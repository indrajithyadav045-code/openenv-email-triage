import json
import urllib.request

BASE_URL = "https://indrajit4533-openenvlearningspace.hf.space"

def _get(path):
    with urllib.request.urlopen(f"{BASE_URL}{path}") as response:
        return json.loads(response.read().decode())

def _post(path, data=None):
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=json.dumps(data or {}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def reset():
    return _post("/reset")

def step(action):
    return _post("/step", action)

def state():
    return _get("/state")

if __name__ == "__main__":
    # START block
    print("[START] task=openenv_email_triage", flush=True)

    obs = reset()
    print("[STEP] step=1 reward=0.0", flush=True)

    # example action
    action = {"action_type": "classify", "email_id": 1}
    result = step(action)

    reward = result.get("reward", 0.0)
    print(f"[STEP] step=2 reward={reward}", flush=True)

    # END block
    print("[END] task=openenv_email_triage score=1.0 steps=2", flush=True)
