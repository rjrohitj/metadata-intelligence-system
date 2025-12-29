“This project documents my journey building a production-style AI system from first principles.”



\# Metadata Intelligence System



A systems-first AI project that enriches raw media metadata using an LLM,

while enforcing strict schemas, validation, and safe fallbacks.



\## What this project demonstrates



\- Explicit data contracts via schemas

\- Defensive validation of inputs and AI outputs

\- Schema-constrained LLM enrichment

\- Safe fallbacks when the model fails

\- Deterministic evaluation using a gold dataset



This is not a demo app. It is an applied AI engineering system.



\## Project structure



metadata\_system/

├── data/

│   ├── sample\_input.json

│   └── gold.json

├── src/

│   ├── main.py

│   ├── schemas.py

│   ├── validator.py

│   ├── llm\_schema.py

│   ├── llm\_client.py

│   └── evaluator.py

└── README.md



\## How to run



\### Requirements

\- Python 3.10+

\- Ollama installed and running

\- An Ollama model pulled (e.g. llama3)



\### Run the system



From the project root:



python -m src.main



The system will:

\- validate input metadata

\- enrich it using an LLM

\- enforce output schemas

\- apply safe fallbacks

\- evaluate results against a gold dataset



\## Why this matters



LLMs are probabilistic and unreliable by default.



This project shows how to integrate them into real systems

without trusting them blindly.

