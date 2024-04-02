# YouTube Video Translator to French

## Introduction
This project allows users to input a YouTube video link and receive a version of the video translated into French, including both the audio and subtitles. Built with a focus on accessibility and ease of use, it integrates advanced machine learning models and libraries to process and translate video content automatically. Additionally, the project features a user interface created using Hugging Face Spaces, facilitating easy interaction with the tool.

## Features
- **Video Translation**: Converts the audio of any YouTube video into French.
- **Subtitles Generation**: Generates French subtitles for the translated video.
- **User Interface**: A simple and intuitive UI built with Hugging Face Spaces, allowing users to easily submit videos for translation.

## How It Works
The project leverages several libraries and APIs to automate the translation process:
- **YouTube Video Processing**: Downloads videos from YouTube using `pytube`.
- **Audio Transcription**: Transcribes audio to text using OpenAI's Whisper model.
- **Translation**: Translates English text to French using the Helsinki-NLP Marian model from the Transformers library.
- **Text-to-Speech**: Converts translated text back into audio using a TTS model for French.
- **Video Editing**: Integrates the new audio and subtitles into the original video, providing a fully translated video.





1. One or two videos with translated audio and translated subtitles embedded in the video. So I made a separate script for that. (link to that script) https://github.com/sohaibchachar/CS370-Project/blob/Milestone5/Milestone5%20(1).ipynb <br> The videos that I generated from that script can be found here  <br>(Video 1) https://drive.google.com/file/d/13macQyqUZMsrpUNwlk93Z9TQtteJ5nuB/view?usp=sharing <br>(Video 2)  https://drive.google.com/file/d/198EWuj-nvhHS3J1bTQqY35c-uJGJccp1/view?usp=sharing <br>
2. Huggingface UI. (Link for that) https://huggingface.co/spaces/sohaibchachar/EnToFrYoutubeVideoTranslator (when you test it please run it with the small videos like 2-3 minutes long because it takes forever for longer videos) <br>

