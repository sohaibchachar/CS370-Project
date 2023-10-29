# %% [markdown]
# # Milestone 1

# %%
from pytube import YouTube, Playlist
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi
save_path = os.path.join("E:","videos")
videos = ["https://www.youtube.com/watch?v=mz51C3Rx6DE&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=67",
            "https://www.youtube.com/watch?v=47aaaFhGtMM&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=80",
            "https://www.youtube.com/watch?v=FmwP-b2rqEc&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=73",
            "https://www.youtube.com/watch?v=rydadItdnt0&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=71",
            "https://www.youtube.com/watch?v=pvlrQHD1etM&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=79",
            "https://www.youtube.com/watch?v=N1vHCOD57Og&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=55",
            "https://www.youtube.com/watch?v=bNKdlnoAqIs&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=27",
            "https://www.youtube.com/watch?v=OvtrnLGeGlM&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=83",
            "https://www.youtube.com/watch?v=bGaHCEZZNMI&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=78",
            "https://www.youtube.com/watch?v=J6ILxNs1CdA&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=68"]
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)            
for url in videos:
    yt = YouTube(url)
    video_id = yt.video_id
    yt_title_sanitized = sanitize_filename(yt.title)

    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if video_stream:
        full_file_path = os.path.join(save_path, yt_title_sanitized + ".mp4")
        print("Downloading to:", full_file_path)
        video_stream.download(output_path=save_path, filename=yt_title_sanitized + ".mp4") 
    caption = YouTubeTranscriptApi.get_transcript(video_id)
    if caption:
        caption_text = "\n".join([f"{c['text']}" for c in caption])
        with open(os.path.join(save_path, yt_title_sanitized + ".txt"), "w", encoding="utf-8") as file:
            file.write(caption_text)       

# %% [markdown]
# 


