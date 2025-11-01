# worker.py
import subprocess, os, json, time

SCANNER_IMAGE = "agentic_scanner:latest"  # built locally from scanner/Dockerfile
TOOL_TIMEOUT = 90

def run_tool(tool, target, job_dir):
    out_path = os.path.join(job_dir, f"{tool}.out")
    cmd = [
        "docker", "run", "--rm",
        "-v", f"{job_dir}:/work",
        SCANNER_IMAGE,
        tool, target, "/work/extra.json"
    ]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=TOOL_TIMEOUT, check=False)
        stdout = p.stdout.decode(errors='ignore')
        stderr = p.stderr.decode(errors='ignore')
    except subprocess.TimeoutExpired:
        stdout = ""
        stderr = f"timeout after {TOOL_TIMEOUT}s"
    with open(out_path, "w") as f:
        f.write("STDOUT:\n")
        f.write(stdout)
        f.write("\n\nSTDERR:\n")
        f.write(stderr)
    return {"tool": tool, "rc": getattr(p, "returncode", -1), "out": out_path}

def run_job_sync(job_id, target, tools, job_dir):
    results = {"job_id":job_id, "target":target, "started": time.time(), "tools": []}
    for t in tools:
        results["tools"].append(run_tool(t, target, job_dir))
    results["finished"] = time.time()
    with open(os.path.join(job_dir, "report.json"), "w") as f:
        json.dump(results, f, indent=2)
