from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware   # ✅ NEW
from pydantic import BaseModel
import uuid, os, subprocess, shutil, json, time

BASE_RESULTS = os.path.abspath("./results")
os.makedirs(BASE_RESULTS, exist_ok=True)

app = FastAPI()

# ✅ Allow frontend on localhost:8080 to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # frontend address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    target: str
    tools: list = ["nmap"]

def sanitize_target(raw: str):
    r = raw.strip()
    if r.startswith("http://") or r.startswith("https://"):
        return r.split("//", 1)[1].split("/", 1)[0]
    return r.split("/", 1)[0]

@app.post("/scan")
def start_scan(req: ScanRequest):
    target = sanitize_target(req.target)
    # basic private IP block (very simple)
    if any(x in target for x in ["127.", "192.168.", "10.", "localhost"]):
        raise HTTPException(status_code=403, detail="private targets blocked")
    job_id = str(uuid.uuid4())
    job_dir = os.path.join(BASE_RESULTS, job_id)
    os.makedirs(job_dir, exist_ok=True)
    meta = {"id": job_id, "target": target, "tools": req.tools, "created": time.time()}
    with open(os.path.join(job_dir, "meta.json"), "w") as f:
        json.dump(meta, f)
    # Synchronous: run worker right away (simple MVP)
    from api.worker import run_job_sync

    run_job_sync(job_id, target, req.tools, job_dir)
    return {"job_id": job_id, "result_url": f"/result/{job_id}"}

@app.get("/result/{job_id}")
def get_result(job_id: str):
    job_dir = os.path.join(BASE_RESULTS, job_id)
    report = os.path.join(job_dir, "report.json")
    if not os.path.exists(report):
        raise HTTPException(status_code=404, detail="report not ready")
    with open(report) as f:
        return json.load(f)
