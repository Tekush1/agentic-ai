just need to run **two commands** — one for the backend (FastAPI) and one for the frontend (static HTML UI).

---

###  Step 1 — Activate your virtual environment & start backend API

```bash
cd ~/agentic-scanner/scanner
source venv/bin/activate
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
```

>  This will start your FastAPI backend (Agentic Scanner API) on
> **[http://localhost:8000](http://localhost:8000)**

---

### Step 2 — In a new terminal, start the frontend (static web UI)

```bash
cd ~/agentic-scanner/scanner/api/static
python3 -m http.server 8080
```

>  This will start your HTML UI on
> **[http://localhost:8080](http://localhost:8080)**

---

### Step 3 — Open in browser:

Go to  **[http://localhost:8080](http://localhost:8080)**
Enter a target like `example.com`, choose `nmap`, and click **Start**

You’ll now see:

```
Mini Scanner (MVP)
Starting...
<scan results will appear here>
```

```
(venv) kush@pop-os:~/agentic-scanner$ tree
.
└── scanner
    ├── agent
    │   └── agent_main.py
    ├── api
    │   ├── app.py
    │   ├── __pycache__
    │   │   └── app.cpython-310.pyc
    │   ├── static
    │   │   └── index.html
    │   └── worker.py
    ├── Dockerfile
    ├── enricher
    │   └── enrich.py
    ├── llm
    │   ├── llm_client.py
    │   └── prompts
    │       └── summarizer_prompt.json
    ├── parsers
    │   └── nmap_parser.py
    ├── results
    │   ├── 5678d7a3-cac2-4712-97c0-986c35165f6a
    │   │   └── meta.json
    │   ├── 6bcc1ff6-84cd-4477-aae1-a921cb1037ca
    │   │   └── meta.json
    │   ├── 7a01db3a-d4e3-45f7-8474-0f64afdb7151
    │   │   └── meta.json
    │   ├── a2c40334-2347-4a3d-84d5-0bc18dc6afe2
    │   │   └── meta.json
    │   ├── a605812b-9622-4ef9-845a-349765e4ba62
    │   │   └── meta.json
    │   ├── ca9ece7c-4289-4c34-95d2-012ca9eab08e
    │   │   └── meta.json
    │   └── nmap_output.xml
    ├── run_tool.sh
    └── venv
```
this is the project structure

---

Would you like me to add a **single shell script** (like `run.sh`) that automatically starts both servers together next time?
