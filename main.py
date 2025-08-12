from fastapi import FastAPI
import uvicorn
import platform
import socket

app = FastAPI(title="NeuroNinjas MCP Server")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/status")
def server_status():
    return {
        "team": "NeuroNinjas",
        "platform": platform.system(),
        "hostname": socket.gethostname(),
        "message": "PuchAI Hackathon Server is running!"
    }

@app.get("/idea")
def project_idea():
    return {
        "problem": "People struggle to find personalized AI-powered solutions they can actually use daily.",
        "solution": "A user-friendly, AI-powered assistant built with PuchAI for practical everyday problem-solving.",
        "status": "Prototype",
        "team": ["Your Name", "Teammate 1", "Teammate 2"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
