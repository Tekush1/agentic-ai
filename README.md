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

---

Would you like me to add a **single shell script** (like `run.sh`) that automatically starts both servers together next time?
