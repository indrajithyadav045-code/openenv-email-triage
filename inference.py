import json
import urllib.request

BASE_URL = "https://indrajit4533-openenvlearningspace.hf.space"

def _get(path):
    try:
        with urllib.request.urlopen(f"{BASE_URL}{path}") as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return {"error": str(e)}

def _post(path, data=None):
    try:
        req = urllib.request.Request(
            f"{BASE_URL}{path}",
            data=json.dumps(data or {}).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return {"error": str(e)}

def reset():
    return _post("/reset")

def step(action):
    return _post("/step", action)

def state():
    return _get("/state")

if __name__ == "__main__":
    print(reset())
