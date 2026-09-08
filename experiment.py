"""Assignment 1: Decoding Experiment

Replace generate() with the approved LLM API/SDK used by your training program.
The prompt must remain identical while testing one parameter at a time.
"""

PROMPT = """Give me 5 ideas for an AI-powered application for a retail company.
Explain each idea in one sentence."""


def generate(**params):
    """Call your organization's approved LLM provider here.

    Expected return: a dict such as
        {"text": "...", "usage": {...}}
    """
    raise NotImplementedError("Connect the approved LLM API/SDK here.")


EXPERIMENTS = [
    {"name": "temperature_0.0", "temperature": 0.0},
    {"name": "temperature_0.3", "temperature": 0.3},
    {"name": "temperature_0.7", "temperature": 0.7},
    {"name": "temperature_1.0", "temperature": 1.0},
]

if __name__ == "__main__":
    print("Prompt:\n", PROMPT)
    print("\nConfigure generate() for your approved model/API before running experiments.")
