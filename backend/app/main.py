from fastapi import FastAPI, UploadFile
from utils.helpers import save_video
from utils.va2speech import video_2_speech

app = FastAPI()


@app.post("/upload-video")
def upload_video(file: UploadFile):
    generated_file_name = save_video(file)
    return video_2_speech(generated_file_name)


@app.get("/search")
def read_root(query: str = ""):
    return query
