from env import EmailEnv, Action

def easy_task():
    env = EmailEnv()
    obs = env.reset()

    total_reward = 0
    done = False

    while not done:
        email = obs.emails[0]

        if email["type"] == "spam":
            action = Action(type="delete", email_id=email["id"])
        else:
            action = Action(type="keep", email_id=email["id"])

        obs, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward