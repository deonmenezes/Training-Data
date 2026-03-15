# NomadicML-style Website + Live API Integration

This project recreates the public NomadicML site flow with original implementation and adds a live API console backed by the official `nomadicml` Python SDK.

## What this includes

- Full single-page marketing site structure (hero, solutions, workflow, products, resources)
- Secure server-side use of `NOMADICML_API_KEY` from `.env`
- API endpoints:
  - `GET /api/health`
  - `GET /api/verify-auth`
  - `POST /api/analyze-url`

## Prerequisites

- Python 3.10+
- A valid NomadicML API key in `.env`

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000`

## API body example

`POST /api/analyze-url`

```json
{
  "video_url": "https://storage.googleapis.com/videolm-bc319.firebasestorage.app/example-videos/Oakland-to-SF-on-Bridge.mp4",
  "custom_event": "Find all instances of ego vehicle straddling two lanes",
  "custom_category": "driving"
}
```

## Notes

- Your existing `.env` is loaded using `python-dotenv`.
- Keep `.env` private and never commit it.
