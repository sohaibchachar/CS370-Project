import os
from TTS.api import TTS
tts = TTS(model_name="tts_models/fr/css10/vits")

def convert_to_speech(text_folder, audio_folder):
    for filename in os.listdir(text_folder):
        
        file_path = os.path.join(text_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            audio_path = os.path.join(audio_folder, filename.replace('.txt', '.mp3'))
            tts.tts_to_file(text=text, file_path=audio_path)
            print(f"Converted {filename} to speech and saved as {audio_path}")

text_folder = 'E:\\NJIT\\Fall 2023\\Intro to AI\\Project\\CS370-Project\\translated_text'
TTS_folder = 'TTS_audio'
os.makedirs(TTS_folder, exist_ok=True)
convert_to_speech(text_folder, TTS_folder)
