from app.agents.workflow import graph


class ApplicationService:

    @staticmethod
    def evaluate(cv_text: str):
        return graph.invoke(
            {
                "cv_text": cv_text
            }
        )