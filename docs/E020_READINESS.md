# E020 synthetic readiness results

These are the fixed synthetic gate results, not MAP evaluation results. No MAP inference or classifier fit has started.

Status: `READY_FOR_MAP_IMPLEMENTATION_CHECK`. Automatic retry: false.

| Checkpoint | Readouts | Binary correct | Insufficient correct | Gate | Tokens/s | Projected MAP hours |
|---|---:|---:|---:|---|---:|---:|
| G15 | 12/12 | 5/10 | 0/2 | True | 2.778534 | 3.805376 |
| G7 | 12/12 | 10/10 | 2/2 | True | 0.716011 | 14.633404 |

The smaller checkpoint has only a technical completion gate; its semantic accuracy is not a stopping criterion.
The 7B gate requires 12/12 completed readouts, at least 8/10 binary fixtures and 2/2 insufficient-information fixtures.
Timings are synthetic-suite projections, not a deadline. No fixture-level decisions or generated text are published.

[Full-precision aggregate receipt](../results/E020_readiness.json)

Aggregate SHA-256: `85a35a6c4ffdfe81323965aac4c4a52048a8b09424b438688c330a7aa3450c6b`.
