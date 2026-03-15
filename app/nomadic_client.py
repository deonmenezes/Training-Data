import os

from dotenv import load_dotenv
from nomadicml import NomadicML
from nomadicml.video import AnalysisType


load_dotenv()


def get_client() -> NomadicML:
    api_key = os.getenv("NOMADICML_API_KEY")
    if not api_key:
        raise ValueError("NOMADICML_API_KEY is missing. Add it to .env")
    return NomadicML(api_key=api_key)


def verify_auth() -> dict:
    client = get_client()
    return client.verify_auth()


def analyze_video_url(
    video_url: str,
    custom_event: str,
    custom_category: str,
) -> dict:
    client = get_client()
    upload_response = client.upload(video_url)
    video_id = upload_response.get("video_id")

    analysis_result = client.analyze(
        video_id,
        analysis_type=AnalysisType.ASK,
        custom_event=custom_event,
        custom_category=custom_category,
    )

    return {"video_id": video_id, "analysis": analysis_result}
