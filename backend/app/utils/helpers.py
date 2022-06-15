from fastapi import UploadFile
import uuid
import os


def save_video(uploaded_file: UploadFile):
    if not uploaded_file.content_type.startswith("video"):
        raise "Cannot process this file !"
    generated_filename = str(uuid.uuid4())
    if not os.path.isdir("videos/"):
        os.mkdir("videos/")
    with open("videos/"+generated_filename, 'wb+') as file_obj:
        file_obj.write(uploaded_file.file.read())
    file_obj.close()
    return generated_filename
