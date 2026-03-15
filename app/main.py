from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .nomadic_client import analyze_video_url, verify_auth
from .schemas import AnalyzeResponse, AnalyzeUrlRequest


app = FastAPI(title="NomadicML Clone App", version="1.0.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", include_in_schema=False)
def root() -> FileResponse:
    return FileResponse("app/static/index.html")


@app.get("/api/health")
def health() -> dict:
    return {"ok": True}


@app.get("/api/verify-auth")
def api_verify_auth() -> dict:
    try:
        auth_info = verify_auth()
        return {"ok": True, "auth": auth_info}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/analyze-url", response_model=AnalyzeResponse)
def api_analyze_url(payload: AnalyzeUrlRequest) -> AnalyzeResponse:
    try:
        result = analyze_video_url(
            video_url=payload.video_url,
            custom_event=payload.custom_event,
            custom_category=payload.custom_category,
        )
        return AnalyzeResponse(video_id=result.get("video_id"), result=result)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
