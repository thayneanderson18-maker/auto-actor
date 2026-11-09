# Greenhouse Jobs Scraper in n8n, Make or plain HTTP

Actor id: `daedal_quintuplet/greenhouse-jobs-scraper`. You need an Apify account and its API token (Apify Console → Settings → Integrations).

## n8n

1. Add the **Apify** node and create an Apify credential with your API token.
2. Choose the operation that runs an Actor and waits for it (named "Run Actor" or similar, depending on the node version). Actor: `daedal_quintuplet/greenhouse-jobs-scraper`.
3. Paste the input as JSON:

```json
{
  "boards": [
    "discord"
  ],
  "maxItems": 50
}
```

4. If the node returns only the run object, add a second Apify node with the "Get dataset items" operation and pass `{{ $json.defaultDatasetId }}`.
5. Send the items wherever you need them: Google Sheets, Airtable, Slack, a database.

## Make

1. Add the **Apify** app, module **Run an Actor**, and turn on "wait for finish".
2. Actor: `daedal_quintuplet/greenhouse-jobs-scraper`. Input JSON: as above.
3. Add **Apify → Get Dataset Items** with the dataset id from the previous module.
4. Map the fields into your sheet, CRM or message.

## Zapier, Pipedream, or any HTTP step

One request runs the actor and returns the results as JSON:

```
POST https://api.apify.com/v2/acts/daedal_quintuplet~greenhouse-jobs-scraper/run-sync-get-dataset-items?token=YOUR_TOKEN
Content-Type: application/json

{
  "boards": [
    "discord"
  ],
  "maxItems": 50
}
```

## No tool at all

In Apify Console open the actor, set the input, then use **Schedules** to run it every morning. Each run's dataset can be downloaded as CSV or Excel, or sent on with Apify's built-in integrations.
