# Routing boundary

This repository uses `gpt-6-sol` as its documented primary target. A multi-model or gateway application may expose more models, but this public draft keeps one verified model contract so examples remain reproducible.

- Resolve the requested model against an allowlist before sending.
- Keep route selection separate from retry policy.
- Log the selected model ID and request ID, never the API key.
- If a target is unavailable, return a visible routing error; do not substitute a different model without an explicit policy.

The live model page controls the current availability and fields.
