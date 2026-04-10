import requests

BASE_URL = "https://indrajit4533-openenvlearningspace.hf.space"

def reset():
    try:
        return requests.post(f"{BASE_URL}/reset").json()
    except Exception as e:
        return {"error": str(e)}

def step(action):
    try:
        return requests.post(f"{BASE_URL}/step", json=action).json()
    except Exception as e:
        return {"error": str(e)}

def state():
    try:
        return requests.get(f"{BASE_URL}/state").json()
    except Exception as e:
        return {"error": str(e)}
