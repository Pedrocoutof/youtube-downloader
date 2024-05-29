# importing packages
from pytube import YouTube
import os


def select_stream(streams):
    for i, stream in enumerate(yt.streams.filter()):
        print("[{}] - {} \t| {} \t| {}mb".format(i + 1, stream.mime_type, stream.resolution, stream.filesize_mb))
    return streams[int(input(">> ")) - 1]


yt = YouTube(str(input("URL: \n>> ")))
#yt.bypass_age_gate()

destination = "./Downloads/"

video = select_stream(yt.streams)

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + "." + video.subtype
os.rename(out_file, new_file)

# result of success
print(yt.title + " foi baixado com sucesso!.")
