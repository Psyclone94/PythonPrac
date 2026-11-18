from fastapi import FastAPI

#Create application instance
app = FastAPI(
    title="AI Engineering API",
    description="My first FastAPI application",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/home")
def health_check():
    return {
        "status": "Healthy",
        "service": "AI Backend"
    }