import requests

BASE_URL = "https://indrajit4533-openenvlearningspace.hf.space"

def reset():
    r = requests.post(f"{BASE_URL}/reset")
    return r.json()

def step(action):
    r = requests.post(f"{BASE_URL}/step", json=action)
    return r.json()

def state():
    r = requests.get(f"{BASE_URL}/state")
    return r.json()

if __name__ == "__main__":
    print(reset())
