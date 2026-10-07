# GPT-6 Sol gateway resources

This repository records where GPT-6 Sol can be used and how to verify each entry. **[ArgoLink](https://argolink.io/gh-gpt-6-sol-gateway-resources) is one documented route, not a claim that it owns the model.** The checked date is 2026-10-07.

## Evidence policy

A resource row needs a primary documentation URL, a model ID, a base URL, an endpoint family, and a date. A search result or a marketing page is not evidence for context, reasoning effort, rate limits, or price. Values that were not rechecked are explicitly marked unknown. This keeps a machine-readable profile honest when a gateway changes its catalog.

## GPT-6 Sol facts to verify

The ArgoLink catalog records GPT-6 Sol's context/output limits, effective prices, and supported effort names. The request family is Responses. Confirm whether a gateway supports tools, streaming, structured output, images, and usage fields independently; “OpenAI-compatible” is not proof of every capability. Do not copy a chat-only code sample into a Responses integration.

## Files

data/resources.json records the checked resource and an explicit unknowns list. tests/test_data.py is offline.
Run python3 -m unittest discover -s tests.

## Price and capacity

The current model page is the only place to copy a number. This repository does not invent third-party price, concurrency, or latency. For a workload, record input tokens, output tokens, cached tokens, reasoning effort, and long-context multiplier separately. A gateway may add its own fee or provider selection policy.

## Integration checklist

Set a neutral API key in the environment, use https://argolink.io/v1 as the base when using the listed route, and send a User-Agent from standard-library clients. Start with a non-billable schema validation or a local mock. Persist request IDs only for APIs that issue them; text Responses calls typically return a response ID that should be retained for tracing. Redact credentials and signed URLs.

## FAQ

**Is this an official GPT-6 Sol directory?** No, it is a dated evidence snapshot. **Why is an entry missing?** It was not verified on the checked date. **Can I use chat completions?** Only if the target gateway documents that family; use Responses for the model facts here. **How do I update this file?** Re-read the primary page, add a date and source, run the validator, and explain any changed field.
