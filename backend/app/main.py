from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from utils.helpers import save_video
from utils.va2speech import video_2_speech
from irengine.elasticsearch import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/upload-video")
def upload_video(file: UploadFile):
    generated_file_name = save_video(file)
    content = video_2_speech(generated_file_name)

    if not is_index_exists():
        create_index()
    else:
        insert_document(generated_file_name, document=content, filename=file.filename)
    return "Document inserted"


@app.get("/search")
def read_root(query: str = ""):
    return search(query)


@app.get("/videos/{video_uuid}")
async def video_endpoint(video_uuid):
    video_path = "videos/" + video_uuid

    return FileResponse(video_path, media_type="video/mp4")
