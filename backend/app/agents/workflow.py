from typing import TypedDict

from langgraph.graph import StateGraph, END


class CandidateState(TypedDict):
    cv_text: str
    analysis: str
    recommendation: str


def analyze_cv(state: CandidateState):
    return {
        "analysis": f"CV analyzed: {state['cv_text']}"
    }


def match_candidate(state: CandidateState):
    return {
        "recommendation": "Backend Developer Internship"
    }


builder = StateGraph(CandidateState)

builder.add_node("cv_analysis", analyze_cv)
builder.add_node("matching", match_candidate)

builder.set_entry_point("cv_analysis")

builder.add_edge("cv_analysis", "matching")
builder.add_edge("matching", END)

graph = builder.compile()