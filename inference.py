import os
from env.environment import TaskEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

env = TaskEnv()

print("[START]")

state = env.reset()
done = False
total_reward = 0

while not done:
    # simple policy: pick first task
    action = state["tasks"][0]["id"]

    next_state, reward, done, _ = env.step(action)

    print(f"[STEP] action={action} reward={reward}")

    total_reward += reward
    state = next_state

print(f"[END] total_reward={total_reward}")