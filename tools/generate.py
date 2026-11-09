"""Render README.md and the per-actor folders from actors.json.

Usage: python3 tools/generate.py   (run from anywhere; paths are relative to the repo root)
Edit actors.json, never the generated files.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER = "daedal_quintuplet"

ACTORS = json.load(open(os.path.join(ROOT, "actors.json"), encoding="utf-8"))

STORE = lambda a: f"https://apify.com/{USER}/{a['name']}"


def indent_block(text, spaces=4):
    """Indent every line after the first, so a JSON literal sits inside an indented call."""
    lines = text.splitlines()
    return "\n".join([lines[0]] + [" " * spaces + l for l in lines[1:]])


def table(rows, headers):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def readme(a):
    inp = table([(f"`{n}`", t, d, f"`{ex}`") for n, t, d, ex in a["input"]], ["Field", "Type", "What it does", "Example"])
    out = table([(f"`{n}`", f"`{ex}`", d) for n, ex, d in a["output"]], ["Field", "Example", "Meaning"])
    others = "\n".join(f"- [{o['title']}]({STORE(o)}): {o['pitch'].split('.')[0]}." for o in ACTORS if o["name"] != a["name"])
    uses = "\n".join(f"- {u}" for u in a["uses"])
    notes = "\n".join(f"- {n}" for n in a["notes"])
    return f"""# {a['title']}

{a['pitch']}

- Store page: {STORE(a)}
- Price: {a['price']}. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `{USER}/{a['name']}`

## Input

{inp}

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

{out}

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/{USER}~{a['name']}/run-sync-get-dataset-items?token=$APIFY_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{json.dumps(a['run_input'])}'
```

## Typical uses

{uses}

## Notes

{notes}

## Our other actors

{others}
"""


def example_py(a):
    return f'''"""Run {a['title']} on Apify and print the results.

    pip install apify-client
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("{USER}/{a['name']}").call(
    run_input={indent_block(json.dumps(a['run_input'], indent=4))}
)

{a.get("var") or ("row" if "trends" in a["name"] else "job")}s = client.dataset(run["defaultDatasetId"]).iterate_items()
for {a.get("var") or ("row" if "trends" in a["name"] else "job")} in {a.get("var") or ("row" if "trends" in a["name"] else "job")}s:
    {a['print_py']}
'''


def example_js(a):
    var = a.get("var") or ("row" if "trends" in a["name"] else "job")
    inp = indent_block(json.dumps(a["run_input"], indent=4))
    return f"""// Run {a['title']} on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const {{ ApifyClient }} = require('apify-client');

async function main() {{
    const client = new ApifyClient({{ token: process.env.APIFY_TOKEN }});

    const run = await client.actor('{USER}/{a['name']}').call({inp});

    const {{ items }} = await client.dataset(run.defaultDatasetId).listItems();
    for (const {var} of items) {{
        {a['print_js']}
    }}
}}

main().catch((err) => {{
    console.error(err);
    process.exit(1);
}});
"""


def n8n_make(a):
    inp = json.dumps(a["run_input"], indent=2)
    return f"""# {a['title']} in n8n, Make or plain HTTP

Actor id: `{USER}/{a['name']}`. You need an Apify account and its API token (Apify Console → Settings → Integrations).

## n8n

1. Add the **Apify** node and create an Apify credential with your API token.
2. Choose the operation that runs an Actor and waits for it (named "Run Actor" or similar, depending on the node version). Actor: `{USER}/{a['name']}`.
3. Paste the input as JSON:

```json
{inp}
```

4. If the node returns only the run object, add a second Apify node with the "Get dataset items" operation and pass `{{{{ $json.defaultDatasetId }}}}`.
5. Send the items wherever you need them: Google Sheets, Airtable, Slack, a database.

## Make

1. Add the **Apify** app, module **Run an Actor**, and turn on "wait for finish".
2. Actor: `{USER}/{a['name']}`. Input JSON: as above.
3. Add **Apify → Get Dataset Items** with the dataset id from the previous module.
4. Map the fields into your sheet, CRM or message.

## Zapier, Pipedream, or any HTTP step

One request runs the actor and returns the results as JSON:

```
POST https://api.apify.com/v2/acts/{USER}~{a['name']}/run-sync-get-dataset-items?token=YOUR_TOKEN
Content-Type: application/json

{inp}
```

## No tool at all

In Apify Console open the actor, set the input, then use **Schedules** to run it every morning. Each run's dataset can be downloaded as CSV or Excel, or sent on with Apify's built-in integrations.
"""


ROOT_README = f"""# Apify actors by {USER}

Working examples for every public actor we run on the [Apify Store](https://apify.com/{USER}). Each folder has a README with the exact input and output fields, a Python example, a Node.js example, and notes for n8n, Make and plain HTTP.

{table([(f"[{a['title']}]({a['name']}/)", a['pitch'].split('.')[0] + '.', a['price'].split('(')[0].strip().rstrip('.'), f"[Store]({STORE(a)})") for a in ACTORS], ["Actor", "What it returns", "Price", "Page"])}

All actors are pay-per-event: you pay per result, nothing per month, and Apify's free plan includes $5 of usage a month.

## Running any of them

1. Create an Apify account and copy your API token (Console → Settings → Integrations).
2. Open the actor's folder here and run `example.py` or `example.js`, or follow `n8n-make.md` for no-code tools.
3. Or make one HTTP call:

```bash
curl -X POST "https://api.apify.com/v2/acts/{USER}~seek-au-job-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{{"keywords": "carpenter", "where": "Brisbane", "maxItems": 50}}'
```

## About this repository

The examples are regenerated from live test runs of each actor, so the fields shown are the fields you get. Found a problem? Open an issue here or on the actor's Store page.

## Maintaining this repository

`actors.json` holds the facts for each actor (fields, examples, pitch, uses, notes). `tools/generate.py` renders everything else from it. To add or update an actor, edit `actors.json` and run:

```bash
python3 tools/generate.py
```
"""

LICENSE = """MIT License

Copyright (c) 2026 thayneanderson18-maker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GITIGNORE = "node_modules/\n__pycache__/\n.env\n*.pyc\n"


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


write(os.path.join(ROOT, "README.md"), ROOT_README)
write(os.path.join(ROOT, "LICENSE"), LICENSE)
write(os.path.join(ROOT, ".gitignore"), GITIGNORE)
for a in ACTORS:
    d = os.path.join(ROOT, a["name"])
    write(os.path.join(d, "README.md"), readme(a))
    write(os.path.join(d, "example.py"), example_py(a))
    write(os.path.join(d, "example.js"), example_js(a))
    write(os.path.join(d, "n8n-make.md"), n8n_make(a))
print("written:", sorted(os.path.relpath(os.path.join(dp, f), ROOT) for dp, _, fs in os.walk(ROOT) if ".git" not in dp for f in fs))
