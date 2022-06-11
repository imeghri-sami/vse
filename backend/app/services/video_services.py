from fastapi import UploadFile
import uuid


def save_video(uploaded_file: UploadFile):
    if not uploaded_file.content_type.startswith("video"):
        raise "Cannot process this file !"
    generated_filename = str(uuid.uuid4())
    with open(generated_filename, 'wb+') as file_obj:
        file_obj.write(uploaded_file.file.read())
    return generated_filename