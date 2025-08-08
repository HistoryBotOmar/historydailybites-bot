import os, subprocess
from TTS.api import TTS

MODEL = "tts_models/en/vctk/vits"   # multi-speaker, natural
SPEAKER = os.getenv("TTS_SPEAKER", "p231")  # try p225,p231,p240,p243
OUT_WAV = os.getenv("OUT_WAV", "voiceover.wav")
TEXT = os.getenv("TTS_TEXT", "This is a Coqui TTS test for History Daily Bites.")

def synthesize(text: str, speaker: str = SPEAKER, out_wav: str = OUT_WAV):
    tts = TTS(model_name=MODEL, progress_bar=False, gpu=False)
    tmp = "voice_tmp.wav"
    tts.tts_to_file(text=text, speaker=speaker, file_path=tmp)
    # Normalize to 48k mono for TikTok
    subprocess.run(["ffmpeg", "-y", "-i", tmp, "-ac", "1", "-ar", "48000", out_wav], check=True)
    os.remove(tmp)
    print("Saved:", os.path.abspath(out_wav))

if __name__ == "__main__":
    synthesize(TEXT, SPEAKER, OUT_WAV)

