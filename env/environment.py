import random

class TaskEnv:
    def __init__(self):
        self.tasks = []
        self.current_step = 0

    def reset(self):
        self.tasks = [
            {"id": 1, "deadline": 5, "duration": 2, "priority": 1},
            {"id": 2, "deadline": 3, "duration": 1, "priority": 2},
            {"id": 3, "deadline": 7, "duration": 3, "priority": 1},
        ]
        self.current_step = 0
        return self.state()

    def state(self):
        return {
            "tasks": self.tasks,
            "step": self.current_step
        }

    def step(self, action):
        reward = 0.0

        task = next((t for t in self.tasks if t["id"] == action), None)

        if task:
            # Base reward
            if task["deadline"] >= task["duration"]:
                reward = 1.0
            else:
                reward = 0.2

            # Bonus for priority
            reward += 0.1 * task["priority"]

            # Penalty for late scheduling
            if task["deadline"] < task["duration"]:
                reward -= 0.2

            self.tasks.remove(task)

        self.current_step += 1
        done = len(self.tasks) == 0

        return self.state(), max(0.0, min(1.0, reward)), done, {}