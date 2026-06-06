from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.agents.workflow import graph

router = APIRouter(prefix="/applications", tags=["applications"])


class ApplicationRequest(BaseModel):
    name: str
    email: EmailStr
    cv_text: str


class ApplicationResponse(BaseModel):
    name: str
    email: EmailStr
    candidate_score: int
    recommended_role: str
    status: str


@router.post("/", response_model=ApplicationResponse)
def create_application(application: ApplicationRequest):
    result = graph.invoke(
        {
            "cv_text": application.cv_text
        }
    )

    return ApplicationResponse(
        name=application.name,
        email=application.email,
        candidate_score=85,
        recommended_role=result.get("recommendation", "Backend Developer Internship"),
        status="interview",
    )