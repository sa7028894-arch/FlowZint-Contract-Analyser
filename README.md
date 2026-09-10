# FlowZint-Contract-Analyser :-
 
A web application that uses GenAI to analyze Solidity smart contracts for potential vulnerabilities and security issues. 
 
## What it does 
- Sign in, then upload a .sol (Solidity) file 
- The file is sent to an LLM (Groq - LLaMA 3.1) with a security-auditor system prompt 
- The model returns a structured severity rating and list of findings (reentrancy, integer overflow, unchecked external calls, access-control issues, etc.) 
- Results are rendered as a report page 
 
## Tech stack 
- Backend: Flask 
- GenAI: Groq API - LLaMA 3.1 
- Frontend: HTML/CSS/JS (vanilla), Bootstrap for the report page 
 
## Setup 
```bash 
cd web_app 
pip install -r requirements.txt 
``` 
 
Set environment variables (never hardcode secrets): 
```bash 
export GROQ_API_KEY="your_groq_api_key" 
export APP_USERNAME="your_chosen_username"    
export APP_PASSWORD="your_chosen_password" 

 
Run it: 
```bash 
python app.py 
``` 
Visit `http://localhost:5000`. 
 
## Tests 
```bash 
pip install -r requirements-dev.txt 
pytest tests/ -v 
``` 
 
## Security note 
An earlier version of this repo had a real email/password hardcoded in app.py and committed to git history. That credential has since been rotated and the code now reads login credentials from environment variables only - nothing sensitive is hardcoded. `debug=True` has also been removed for safe deployment. 
