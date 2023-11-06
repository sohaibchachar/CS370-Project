from moviepy.editor import VideoFileClip
from whisper import load_model
import os
import glob

def audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, verbose=False, logger=None)

def text_from_audio(audio_path, text_path, model):
    result = model.transcribe(audio_path)
    with open(text_path, 'w') as file:
        file.write(result["text"])


folder_path = "/content/drive/MyDrive/Colab Notebooks/CS370_project/videos"
text_folder = os.path.join(folder_path, "text")
audio_folder = os.path.join(folder_path, "audio")


model = load_model("base")

videos = glob.glob(os.path.join(folder_path, "*.mp4"))

for video_path in videos:

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(audio_folder, video_name + ".mp3")
    text_path = os.path.join(text_folder, video_name + ".txt")
    audio_from_video(video_path, audio_path)
    print("Audio file saved to", audio_path)
    text_from_audio(audio_path, text_path, model)
    print("Transcription saved to", text_path)


