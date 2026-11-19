from fastapi import FastAPI,HTTPException
from app.models.agent import AGENT_STORE,AgentState

app=FastAPI(
    title="AI FDE API",
    description="Python practice API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message":"Welcome to the agentic app"}

@app.get("/health")
def home():
    return {"message":"Health is perfect for this app"}

@app.get("/about")
def home():
    return {"message":"This app is all about practice"}

@app.get("/agents")
def get_agents(status:AgentState | None=None):
    if status is None:
     return list(AGENT_STORE.values())

    return[
        agent
        for agent in AGENT_STORE.values()
        if agent.status == status
    ]

@app.get("/agents/{agent_id}")
def list_agents_by_agent_id(agent_id:str):
    agent=AGENT_STORE.get(agent_id)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail=f"Agent {agent_id} not found"
        )
    return agent

