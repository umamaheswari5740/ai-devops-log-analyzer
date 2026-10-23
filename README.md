

\# AI-Powered DevOps Log Analyzer



A local AI application that analyzes Linux and application logs and

provides possible causes and troubleshooting recommendations.



\## Features



\- Paste logs or upload `.log` and `.txt` files

\- Local inference using Ollama and Qwen2.5 3B

\- Formatted Markdown analysis

\- File validation and input limits

\- Basic automated tests



\## Technologies



\- Python

\- Flask

\- Ollama

\- Qwen2.5 3B

\- HTML and CSS

\- pytest

\- Git



\## Prerequisites



\- Python 3.11 or compatible

\- Git

\- Ollama

\- The `qwen2.5:3b` model



\## Setup on Windows



1\. Install Python and Ollama.

2\. Download the model:



&#x20;  `ollama pull qwen2.5:3b`



3\. Create a virtual environment:



&#x20;  `python -m venv .venv`



4\. Install dependencies:



&#x20;  `.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt`



5\. Start the application:



&#x20;  `.\\.venv\\Scripts\\python.exe app.py`



6\. Open http://127.0.0.1:5000



\## Run tests



`.\\.venv\\Scripts\\python.exe -m pytest -v`



\## Architecture



Browser → Flask application → Ollama local API → Qwen2.5 3B



\## Limitations



AI output may be inaccurate. Verify troubleshooting suggestions before

applying them to real systems. Do not upload sensitive production logs.



\## Project status



Local prototype. Further security, usability, and deployment improvements

are required before production use.



