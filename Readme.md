---
title: OpenEnv Email Triage
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# OpenEnv Email Triage Environment

## 📌 Overview

This project implements a real-world OpenEnv environment that simulates an email inbox triage workflow. An AI agent interacts with the environment to manage emails by deleting spam, keeping important messages, and organizing the inbox efficiently.

The environment follows the OpenEnv specification with structured observation, action, and reward models, along with step(), reset(), and state() APIs.

---

## 🎯 Motivation

Email triage is a common real-world task. Automating inbox management using AI agents helps:

* Reduce manual effort
* Improve productivity
* Prioritize important communication
* Filter spam automatically

This environment provides a simplified but realistic simulation for training and evaluating AI agents.

---

## 🧠 Environment API

### reset()

Initializes the environment and returns the starting observation.

### step(action)

Executes an action and returns:

* observation
* reward
* done
* info

### state()

Returns the current environment state.

---

## 📥 Observation Space

```
{
  "emails": [
    {
      "id": int,
      "text": string,
      "type": "spam | important | normal"
    }
  ],
  "unread_count": int
}
```

---

## 🎮 Action Space

```
{
  "type": "delete | keep",
  "email_id": int
}
```

---

## 🏆 Reward Function

| Action         | Reward |
| -------------- | ------ |
| Delete spam    | +0.3   |
| Keep important | +0.3   |
| Wrong action   | -0.2   |
| Inbox cleared  | +1.0   |

The reward function provides partial progress signals and penalizes incorrect actions.

---

## 🧪 Tasks

### Easy

* Small inbox
* Clear spam vs important emails
* Goal: clean inbox correctly

### Medium

* Mixed email priorities
* Requires decision making

### Hard

* Ambiguous messages
* Requires optimal sequence of actions

---

## ▶️ Baseline Inference

Run locally:

```
python run.py
```

Example output:

```
Score: 1.4
```

---

## 🐳 Docker Support

Build container:

```
docker build -t openenv-email .
```

Run container:

```
docker run openenv-email
```

---

## ⚙️ Requirements

```
pydantic
```

---

## 📂 Project Structure

```
.
├── env.py
├── tasks.py
├── run.py
├── Dockerfile
├── requirements.txt
├── openenv.yaml
└── README.md
```

---

## 🚀 Deployment

This environment is containerized and deployed using Docker and hosted online.

---

## ✅ Features

* Real-world task simulation
* OpenEnv API compliance
* Structured observation/action models
* Multi-task setup (easy → hard)
* Reward shaping
* Docker container support
* Baseline scoring script

---

## 📊 Baseline Score

```
Score: 1.4
```

---

## 👨‍💻 Author

Indrajit Yadav.M
HariNandhan.P.S
Siddarth.M
---

## 📄 License

MIT License
