from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

app = FastAPI(title="AI Influence Orchestrator")

# Routers for modularity (to expand: agents, status, analytics, etc.)
api_router = APIRouter()

@app.get("/")
def health():
      return {"status": "ok", "message": "AI-Influence backend is running"}

# Example pipeline endpoint (stub)
@api_router.post("/pipeline/run")
def run_pipeline(task: dict):
      # Logic for dispatching tasks to agents/bots will go here
      return JSONResponse({"result": "Pipeline execution started", "task": task})

app.include_router(api_router, prefix="/api")
