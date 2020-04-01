import webbrowser
import os
import subprocess
import random

greetIntent = ["hi", "hello", "namaste", "bonjour", "hola", "johar", "hiii"]
playIntent = ["play a song", "play some random song", "play a bollywood song"]

while True:
    message = input("Enter your message : ")

    # if message == "hi" or message == "hello" or message == "hiiii" or message == "namaste" or message == "bonjour" or message == "hola":
    if message in greetIntent:
        print("Hello, how are you ? ")

    elif message == "I am fine" or message == "not good":
        print("I am fine too!")

    elif message.startswith("open"):
        websiteName = message.split()[1]
        webbrowser.open(f"http://www.{websiteName}.com")

    elif message.startswith("run"):
        appName = message.partition(' ')[-1]
        # os.startfile(f"{appName}.exe")
        subprocess.call(["open", '/Applications/SketchBook.app'])

    elif message in playIntent:
        # print(os.getcwd())
        os.chdir(
            "/Users/anmolrajarora/Documents/adv-python-reg-dec/MusicPlayer/songs")
        # print(os.getcwd())
        # print(os.listdir())
        songs = os.listdir()
        selectedSong = random.choice(songs)
        # os.startfile(selectedSong)
        print("Playing", selectedSong)
        subprocess.call(["open", selectedSong])

    elif message == "bye":
        print("See you soon..")
        quit()

    else:
        print("I don't understand!")

# open facebook -> ["open", "facebook"]
# open google

# run eclipse
# run github desktop
# run visual studio code
