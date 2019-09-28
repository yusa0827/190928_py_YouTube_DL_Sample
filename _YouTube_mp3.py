import youtube_dl

# URLの入力
print('#ぴこぴミュージックがはじまるよ#')
while True:
    # URLを入力
    URL_ = input("""聞きたいYouTubeの音楽のURLを入力してください
URL = """)

    # ファイル名の入力
    NAME = input("""保存したいファイル名を入力してください
NAME = """)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':  NAME + '.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
             'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(URL_, download=True)

    # 続けるか確認
    check_ = input("""続けますか? Yes:1 No:0
Answer = """)

    if int(check_) != 1:
        break
