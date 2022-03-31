import asyncio
import sys
from mega import Mega
from pytube import YouTube
import time

list = [
]
mega = Mega()
m = mega.login('yifeca5778@kuruapp.com', 'Israr@1990')


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50 - done)))
    sys.stdout.flush()


def saveMega(stream, path):
    time.sleep(30)
    print("done")
    print(m.get_storage_space(giga=True))
    file = m.upload(path)
    print(m.get_upload_link(file))


async def downloadYouTube(videourl):
    yt = YouTube(videourl, on_progress_callback=progress_func)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # name = yt.get_file_path()
    yt.download()


if __name__ == '__main__':

    for i in list:
        asyncio.run(downloadYouTube(i))
    #    downloadYouTube(link)
