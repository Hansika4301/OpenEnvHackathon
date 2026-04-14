import os
from openai import OpenAI
from env.environment import TaskEnv

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

env = TaskEnv()

print("[START]")

state = env.reset()
done = False
total_reward = 0

while not done:
    # Convert state to prompt
    prompt = f"Tasks: {state['tasks']}. Choose the best task id."

    try:
        # LLM call
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content.strip()

        # Extract number safely
        action = int(''.join(filter(str.isdigit, content)))

        # Validate action
        valid_ids = [t["id"] for t in state["tasks"]]
        if action not in valid_ids:
            action = valid_ids[0]

    except Exception:
        # Fallback if anything fails
        action = state["tasks"][0]["id"]

    # Step in environment
    next_state, reward, done, _ = env.step(action)

    print(f"[STEP] action={action} reward={reward}")

    total_reward += reward
    state = next_state

print(f"[END] total_reward={total_reward}")