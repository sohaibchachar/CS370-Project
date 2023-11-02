FROM python:3.11.6-slim

COPY . /app

RUN pip install pytube

RUN pip install youtube_transcript_api



EXPOSE 8888
WORKDIR /app

CMD ["python", "Milestone1.py"]  
