from fastapi import FastAPI
from env import EmailEnv, Action
import uvicorn

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"message": "OpenEnv Email Triage API running"}

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


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
