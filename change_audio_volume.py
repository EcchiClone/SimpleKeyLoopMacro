import pydub
pydub.AudioSegment.converter = r"F:\\ffmpeg-20200608-d29aaf1-win64-static\\bin\\ffmpeg.exe"
pydub.AudioSegment.ffprobe = r"F:\\ffmpeg-20200608-d29aaf1-win64-static\\bin\\ffmpeg.exe"
song = pydub.AudioSegment.from_mp3("complete.mp3")
end = song - 5
end.export("complete_5.mp3", format="mp3")

# fail