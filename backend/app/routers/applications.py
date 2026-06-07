from fastapi import APIRouter

from app.models.application import Application, ApplicationResponse
from app.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("/", response_model=ApplicationResponse)
def create_application(application: Application):
    result = ApplicationService.evaluate(application.cv_text)

    return ApplicationResponse(
        name=application.name,
        email=application.email,
        candidate_score=result.get("candidate_score", 85),
        recommended_role=result.get(
            "recommendation",
            "Backend Developer Internship",
        ),
        status="interview",
    )