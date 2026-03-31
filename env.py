from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    emails: List[dict]
    unread_count: int

class Action(BaseModel):
    type: str
    email_id: int

class EmailEnv:

    def __init__(self):
        self.emails = []
        self.done = False

    def reset(self):
        self.emails = [
            {"id": 1, "text": "Buy now spam offer", "type": "spam"},
            {"id": 2, "text": "Meeting at 5pm", "type": "important"},
            {"id": 3, "text": "Hello just checking", "type": "normal"},
        ]
        self.done = False
        return self.state()

    def state(self):
        return Observation(
            emails=self.emails,
            unread_count=len(self.emails)
        )

    def step(self, action: Action):
        reward = 0.0

        for email in self.emails:
            if email["id"] == action.email_id:

                if action.type == "delete" and email["type"] == "spam":
                    reward += 0.3

                elif action.type == "keep" and email["type"] == "important":
                    reward += 0.3

                else:
                    reward -= 0.2

                self.emails.remove(email)
                break

        if len(self.emails) == 0:
            self.done = True
            reward += 1.0

        return self.state(), reward, self.done, {}