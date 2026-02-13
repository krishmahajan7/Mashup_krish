import os
import shutil
from yt_dlp import YoutubeDL
from pydub import AudioSegment


# -------------------- Download Audios Directly --------------------
def download_audios(singer, num_videos):
    search_query = f"ytsearch{num_videos}:{singer} songs"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/audio_%(id)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    os.makedirs("audios", exist_ok=True)

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


# -------------------- Cut Audio --------------------
def cut_audio(duration):
    os.makedirs("cuts", exist_ok=True)

    for file in os.listdir("audios"):
        audio_path = os.path.join("audios", file)

        audio = AudioSegment.from_mp3(audio_path)
        cut_part = audio[:duration * 1000]

        cut_part.export(os.path.join("cuts", file), format="mp3")


# -------------------- Merge Audios --------------------
def merge_audios(output_file):
    final_audio = AudioSegment.empty()

    for file in sorted(os.listdir("cuts")):
        audio_path = os.path.join("cuts", file)
        audio = AudioSegment.from_mp3(audio_path)
        final_audio += audio

    final_audio.export(output_file, format="mp3")


# -------------------- Clean Temporary Folders --------------------
def clean_folders():
    for folder in ["audios", "cuts"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)


# -------------------- MAIN FUNCTION FOR FLASK --------------------
def create_mashup(singer, num_videos, duration, output_file="mashup.mp3"):
    try:
        if num_videos <= 10:
            raise ValueError("Number of videos must be greater than 10.")

        if duration <= 20:
            raise ValueError("Duration must be greater than 20 seconds.")

        download_audios(singer, num_videos)
        cut_audio(duration)
        merge_audios(output_file)

        clean_folders()

        return output_file

    except Exception as e:
        clean_folders()
        raise Exception(f"Mashup creation failed: {str(e)}")
