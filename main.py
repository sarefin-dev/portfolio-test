from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Portfolio Test", version="1.0.0")


class HealthResponse(BaseModel):
    status: str
    message: str


@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}


@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="healthy", message="Service is running")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
