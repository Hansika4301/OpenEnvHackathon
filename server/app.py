from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from env.environment import TaskEnv

# CREATE app FIRST
app = FastAPI()
env = TaskEnv()

# UI ROUTE
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Task Scheduler</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 40px;
            }
            h1 {
                color: #38bdf8;
            }
            .card {
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
            }
            button {
                background: #38bdf8;
                border: none;
                padding: 10px 20px;
                margin: 10px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background: #0ea5e9;
            }
            pre {
                background: black;
                padding: 10px;
                border-radius: 8px;
                text-align: left;
                overflow-x: auto;
                color: #22c55e;
            }
        </style>
    </head>
    <body>
        <h1>OpenEnv Task Scheduler</h1>
        <div class="card">
            <p>AI-based task scheduling using deadlines, duration, and priority</p>
            <button onclick="resetEnv()">Reset</button>
            <button onclick="getState()">Get Tasks</button>
            <h3>Task Data:</h3>
            <pre id="output">Click a button to see tasks...</pre>
        </div>
        <script>
            function formatTasks(data) {
                if (!data.tasks) return JSON.stringify(data, null, 2);
                let text = "";
                data.tasks.forEach(t => {
                    text += "Task " + t.id +
                            " | Deadline: " + t.deadline +
                            " | Duration: " + t.duration +
                            " | Priority: " + t.priority + "\\n";
                });
                return text;
            }
            async function resetEnv() {
                const res = await fetch('/reset', {method: 'POST'});
                const data = await res.json();
                document.getElementById("output").innerText = formatTasks(data);
            }
            async function getState() {
                const res = await fetch('/state');
                const data = await res.json();
                document.getElementById("output").innerText = formatTasks(data);
            }
        </script>
    </body>
    </html>
    """

# API ROUTES
@app.post("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: int):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

# REQUIRED FOR OPENENV
def main():
    return app

# RUN BLOCK
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)