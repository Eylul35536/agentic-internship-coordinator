from fastapi import FastAPI

from app.agents.workflow import graph

app = FastAPI(title="Agentic Internship Coordinator")


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.get("/test-agent")
def test_agent():
    result = graph.invoke(
        {
            "cv_text": "Python developer with FastAPI experience"
        }
    )

    return result