'''
Script to download a playlist from YouTube in m4a format.
'''


from yt_dlp import YoutubeDL


OUTPUT_DIR = 'songs/'

playlist_url = input("Playlist URL: ")

options = {
    'format': 'm4a/bestaudio/best',
    'outtmpl': f'{OUTPUT_DIR}%(title)s.%(ext)s',
    'addmetadata': True,
    'writethumbnail': True,
    'postprocessors': [
        {
            'key': 'FFmpegMetadata',
        },
        {
            'key': 'EmbedThumbnail',
        },
        {
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'm4a',
        },
    ],
}

with YoutubeDL(options) as ydl:
    error_code = ydl.download(playlist_url)