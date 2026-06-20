# Training-Data (NomadicML Clone App)

A FastAPI application that recreates the NomadicML public site flow and provides a live API console backed by the official `nomadicml` Python SDK.

## Tech Stack

- **Framework:** FastAPI (Python)
- **Server:** Uvicorn (ASGI)
- **ML SDK:** NomadicML (`nomadicml`)
- **Validation:** Pydantic v2
- **Config:** `python-dotenv`
- **Frontend:** Static HTML/CSS/JS served by FastAPI

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file at the project root:
```
NOMADICML_API_KEY=your_key_here
```

## Build / Run / Test

```bash
# Run the development server (from project root)
uvicorn app.main:app --reload
```

Server runs at `http://localhost:8000` by default.

## Project Structure

```
Training-Data/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app, route definitions
│   ├── nomadic_client.py # NomadicML SDK wrapper (analyze_video_url, verify_auth)
│   ├── schemas.py        # Pydantic request/response models
│   └── static/           # Static frontend assets (HTML/CSS/JS)
├── requirements.txt
└── README.md
```

## Architecture & Key Files

- `app/main.py` — entry point; mounts static files and defines API routes (`/api/health`, `/api/verify-auth`, `/api/analyze-url`).
- `app/nomadic_client.py` — wraps the `nomadicml` SDK calls; keep API key usage here.
- `app/schemas.py` — Pydantic models for request/response validation.
- `app/static/` — the frontend; served at `/` via `FileResponse`.

## Conventions & Notes for Agents

- The app is launched as `uvicorn app.main:app`; the `app` directory is a Python package.
- `NOMADICML_API_KEY` is required in `.env` for any API calls that hit the NomadicML backend to work.
- All NomadicML SDK interactions are isolated in `nomadic_client.py` — extend there, not in `main.py`.
- This is a single-process ASGI app; no task queue or background worker is set up.
