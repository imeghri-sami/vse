FROM python:3.9

WORKDIR /backend

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir ./app

COPY ./app ./app

RUN cd ./app

CMD ["uvicorn", "main:app"]