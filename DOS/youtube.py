import youtube_dl

link = [input("Link do vídeo: ")]
if link == [""]:
    link =["https://www.youtube.com/watch?v=36eyJyhsjkc&ab_channel=SrShadowsombr%C3%ADo"]


with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)
