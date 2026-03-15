from pydantic import BaseModel, Field


class AnalyzeUrlRequest(BaseModel):
    video_url: str = Field(..., description="Publicly accessible video URL")
    custom_event: str = Field(
        default="Find all instances of ego vehicle straddling two lanes"
    )
    custom_category: str = Field(default="driving")


class AnalyzeResponse(BaseModel):
    video_id: str | None = None
    result: dict
