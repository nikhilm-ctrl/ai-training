# AI Training

## Assignment 1 — Generation & Parameters: Decoding Experiment

### Objective
Run the same prompt across multiple generation configurations and compare how decoding parameters affect determinism, creativity, repetition, output length, and production suitability.

### Prompt
> Give me 5 ideas for an AI-powered application for a retail company. Explain each idea in one sentence.

### Parameters explored
- Temperature
- Top-P
- Top-K (where supported)
- Frequency penalty (where supported)
- Maximum completion/output tokens
- Structured output

### Experiment design
Change one parameter at a time where practical. Keep the model, prompt, system instructions, and other parameters constant so that changes can be attributed to the parameter being tested.

### Key concepts
- **Temperature:** changes the sharpness of the sampling distribution and therefore output variability.
- **Top-K:** limits sampling to the K highest-probability candidate tokens.
- **Top-P:** keeps the smallest set of candidate tokens whose cumulative probability reaches P.
- **Frequency penalty:** discourages repeated tokens based on how frequently they have already appeared.
- **Max completion tokens:** bounds the maximum generated output length.
- **Structured output:** constrains responses to a defined structure/schema, making them easier for software to consume reliably.

### Production takeaway
There is no universally best decoding configuration. The right settings depend on the use case. Production reliability also requires validation, evaluation, monitoring, guardrails, and sensible latency/cost limits—not just a low temperature.

### Results
`results.csv` contains the experiment log template. Actual model outputs should be recorded using the model/API provided by the training program. Outputs are intentionally not fabricated.
