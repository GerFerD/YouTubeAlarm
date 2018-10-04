import webbrowser
import random

def choose_song():
    return song_list[random.randint(0,2)]

song_list = ["https://www.youtube.com/watch?v=UJFYOkQDB20", "https://www.youtube.com/watch?v=MkD_kYkRk3c", "https://www.youtube.com/watch?v=HrLjbJtMfVk"]

webbrowser.open(choose_song())