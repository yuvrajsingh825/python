songs = [
    "Song1",
    "Song2",
    "Song3"
]

playlist = iter(songs)

while True:
    try:
        print(next(playlist))
    except StopIteration:
        print("Playlist End")
        break
git 