
""""
uvicorn main:app --host 0.0.0.0 --port 10000 

https://spacebartechnologies.retool.com/api/file/05fbb12b-f5c9-4a16-b8ba-855f58a1679f
"""

from fastapi import FastAPI
from pydantic import BaseModel
from moviepy.video.io.VideoFileClip import VideoFileClip
from typing import List


app = FastAPI()

class VideoClip(BaseModel):
    url: str

videos: List[VideoClip] = []

@app.get("/")
def welcome_message():
    return {"message": "Welcome To calculate video duration api."}

@app.post("/videos")


def calculate_duration(video: VideoClip):
    clip = VideoFileClip(video.url)
    duration = clip.duration
    return {"url": video.url,
        "duration_seconds": duration}