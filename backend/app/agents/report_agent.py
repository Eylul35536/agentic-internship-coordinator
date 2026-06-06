def generate_report(state):
    return {
        "report": (
            f"Candidate score: {state['candidate_score']}. "
            f"Recommended role: {state['recommendation']}."
        )
    }