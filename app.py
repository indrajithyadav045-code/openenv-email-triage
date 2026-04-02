from fastapi import FastAPI
from env import EmailEnv, Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs,
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }

@app.get("/state")
def state():
    return env.state()
