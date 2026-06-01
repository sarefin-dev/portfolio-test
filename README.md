# Portfolio Test

A simple FastAPI project with hello world and health check endpoints.

## Setup

### Install dependencies with uv

```bash
uv sync
```

### Run the application

```bash
uv run python main.py
```

Or with uvicorn directly:

```bash
uv run uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Hello world endpoint
- `GET /health` - Health check endpoint

## Access the API

- API: http://localhost:8000
- Docs (Swagger UI): http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
