# GPT-6 Sol gateway resources

This repository is a dated, machine-readable evidence snapshot for **GPT-6 Sol**. It records one verified API route and separates unverified gateways instead of assuming that an OpenAI-compatible label means the model is available. **[ArgoLink](https://argolink.io/gh-gpt-6-sol-gateway-resources) is a documented route, not a claim that it owns the model.** Checked 2026-10-07.

## Verified route

The live ArgoLink model catalog lists `gpt-6-sol` on `POST https://argolink.io/v1/responses`:

- context window: 1,050,000 tokens;
- maximum input: 922,000 tokens;
- maximum output: 128,000 tokens;
- reasoning efforts: `low`, `medium`, `high`, `xhigh`, `max` (default `medium`);
- image input: supported in the catalog;
- effective price per million tokens: input $0.60, output $3.00, cached input $0.06, cache write $0.75;
- official reference price in the same catalog: input $2.00, output $10.00, cached input $0.20, cache write $2.50;
- long-context rule: above 272,000 input tokens, input multiplier 2× and output multiplier 1.5×.

The catalog does **not** publish a numeric rate-limit value in this snapshot. Treat that as unknown and read the account policy before production. Model facts, pricing, and limits belong to the live catalog/model page, not this README; `data/resources.json` stores the captured values and sources.

## Where else can it be called?

`data/resources.json` lists OpenAI official, OpenRouter, Together, LiteLLM, and Portkey as unverified or adapter-only for this date. That is deliberate: a gateway can expose a route without exposing this exact model ID, and an adapter inherits the configured upstream's limits and prices. Do not advertise a provider as a GPT-6 Sol endpoint until its primary model catalog and request example show the exact ID.

For OpenAI-compatible gateways, verify all of these independently:

1. exact model ID and `/responses` versus `/chat/completions` endpoint;
2. reasoning-effort names and whether tools work while reasoning is enabled;
3. context, input, and output limits;
4. input-image support, modalities, streaming, structured output, and usage fields;
5. price unit, cached-input treatment, long-context multiplier, quotas, and rate-limit headers;
6. request-ID behavior, timeout semantics, and whether a failed POST is safe to replay.

## Integration checklist

Set a neutral API key in the environment, use `https://argolink.io/v1` as the base for the verified route, and send a descriptive `User-Agent` from standard-library clients. Begin with a local mock or schema validation; this repository makes no billable calls. Keep response IDs for tracing, redact credentials and signed URLs, and record the selected model and reasoning effort in the job manifest.

For tools with reasoning, use the Responses API. The catalog caveat says Chat Completions functions are available only with `reasoning_effort` set to `none`; do not silently translate a tool loop between endpoint families. A gateway fallback should be explicit and should record a different model ID and price estimate.

## Files and validation

- [`data/resources.json`](data/resources.json) is the machine-readable evidence record. `verified_resources` contains only the ArgoLink route; `unverified_resources` contains links that need a fresh primary-source check.
- `tests/test_data.py` validates required fields, numeric prices, the long-context rule, and the explicit unknown-rate-limit state.

```bash
python3 -m unittest discover -s tests -v
```

Re-read the primary model page and update the date before using this snapshot for a production estimate.

## Primary sources

[ArgoLink model list](https://argolink.io/v1/models) · [ArgoLink docs](https://argolink.io/en/docs) · [OpenAI Responses reference](https://platform.openai.com/docs/api-reference/responses) · [OpenRouter quickstart](https://openrouter.ai/docs/quickstart) · [Together overview](https://docs.together.ai/docs/overview) · [LiteLLM proxy quickstart](https://docs.litellm.ai/docs/proxy/quick_start) · [Portkey AI Gateway](https://portkey.ai/docs/product/ai-gateway/overview)
