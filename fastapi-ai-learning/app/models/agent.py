from dataclasses import dataclass,field
from enum import Enum

class AgentState(str,Enum):
    ACTIVE="active"
    IDLE="idle"
    MAINTENANCE="maintenance"

@dataclass
class Agent:
    id:str
    name:str
    role:str
    status:AgentState
    model:str
    avg_latency_ms:int
    tasks_completed:int
    capabilities:list[str] = field(default_factory=list)

AGENT_STORE: dict[str,Agent] = {
    "concept-explainer":Agent(
        id="concept-explainer",
        name="Concept Explainer",
        role="Break down tough topics with sample examples",
        status=AgentState.ACTIVE,
        model="gemini-2.5-flash",
        avg_latency_ms=420,
        tasks_completed=128,
        capabilities=["analogies","step by step breakdown","examples"]
    ),
    "pyq-solver":Agent(
            id="pyq-solver",
            name="PYQ Solver",
            role="Walks through previous year question paper with marking schemes",
            status=AgentState.IDLE,
            model="gemini-2.5-pro",
            avg_latency_ms=167,
            tasks_completed=345,
            capabilities=["exam-solution","hint mode","schemes"]
        ),
    "flashcard-maker":Agent(
            id="flashcard-maker",
            name="Flashcard Maker",
            role="Generate quick revision card for notes",
            status=AgentState.MAINTENANCE,
            model="gemini-2.5-flash",
            avg_latency_ms=224,
            tasks_completed=118,
            capabilities=["cloze-cards","key-terms","space-repitition"]
        ),
    "code-reviewer":Agent(
            id="code-reviewer",
            name="Code Reviewer",
            role="Reviews code base and provide suggesions",
            status=AgentState.ACTIVE,
            model="gemini-2.5-pro",
            avg_latency_ms=98,
            tasks_completed=562,
            capabilities=["bug-detection","complexity-check","suggestions"]
        )
}