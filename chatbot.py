import webbrowser
import os
import subprocess
import random
from datetime import datetime

greetIntent = ["hi", "hello", "namaste", "bonjour", "hola", "johar", "hiii"]
playIntent = ["play a song", "play some random song", "play a bollywood song"]
dateIntent = ["date please", "what's the date today", "today's date please"]
timeIntent = ["please tell me the time",
              "what's the time", "current time please"]

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
        print('''
        1. Play a random song
        2. Play a specific song
        ''')
        userChoice = int(input("Enter your choice : "))
        if userChoice == 1:
            selectedSong = random.choice(songs)
        elif userChoice == 2:
            for i in range(len(songs)):
                print(f"{i + 1}. {songs[i]}")
            userChoice = int(input("Enter song number : "))
            selectedSong = songs[userChoice - 1]
        # os.startfile(selectedSong)
        print("Playing", selectedSong)
        subprocess.call(["open", selectedSong])

    elif message.startswith("play"):
        pass

    elif message in timeIntent:
        obj = datetime.now()
        print(obj.strftime("%H:%M:%S"))

    elif message in dateIntent:
        obj = datetime.now()
        print(obj.strftime("%a %b %d %H:%M:%S %Y"))

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

'''
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> type(datetime)
<class 'module'>
>>> type(datetime.datetime)
<class 'type'>
>>> datetime.datetime()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    datetime.datetime()
TypeError: function missing required argument 'year' (pos 1)
>>> datetime.datetime().now()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    datetime.datetime().now()
TypeError: function missing required argument 'year' (pos 1)
>>> datetime.datetime.now()
datetime.datetime(2020, 4, 2, 14, 8, 25, 346258)
>>> type(datetime.datetime.now)
<class 'builtin_function_or_method'>
>>> obj = datetime.datetime.now()
>>> type(obj)
<class 'datetime.datetime'>
>>> obj.strftime("%A")
'Thursday'
>>> obj.strftime("%a")
'Thu'
>>> obj.strftime("%B")
'April'
>>> obj.strftime("%b")
'Apr'
>>> obj.strftime("%C")
'20'
>>> obj.strftime("%c")
'Thu Apr  2 14:09:28 2020'
>>> obj.strftime("%D")
'04/02/20'
>>> obj.strftime("%d")
'02'
>>> obj.strftime("%M")
'09'
>>> obj.strftime("%m")
'04'
>>> obj.strftime("%y")
'20'
>>> obj.strftime("%Y")
'2020'
>>> obj.strftime("%H")
'14'
>>> obj.strftime("%h")
'Apr'
>>> obj.strftime("%HH")
'14H'
>>> obj.strftime("%M")
'09'
>>> obj.strftime("%S")
'28'
>>> obj.strftime("%P")
'P'
>>> obj.strftime("%p")
'PM'
>>> # 'Thu Apr  2 14:09:28 2020'
>>> obj.strftime("%a %b %d %H:%M:%S %Y")
'Thu Apr 02 14:09:28 2020'
>>> obj.strftime("%c")
'Thu Apr  2 14:09:28 2020'
>>> import datetime
>>> from datetime import datetime
>>> type(datetime)
<class 'type'>
>>> datetime.now()
datetime.datetime(2020, 4, 2, 14, 33, 45, 11262)
>>> datetime(2008, 11, 26, 20)
datetime.datetime(2008, 11, 26, 20, 0)
>>> obj2 = datetime(2008, 11, 26, 20)
>>> obj2.strftime("%a %b %d %H:%M:%S %Y")
'Wed Nov 26 20:00:00 2008'
>>> obj.strftime("%H")
'14'
>>> obj.strftime("%h")
'Apr'
'''

'''
from datetime import datetime
>>> datetime.now()
datetime.datetime(2020, 4, 2, 14, 53, 32, 467372)
>>> date
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    date
NameError: name 'date' is not defined
>>> from datetime import date
>>> date
<class 'datetime.date'>
>>> from datetime import *
>>> datetime
<class 'datetime.datetime'>
>>> date
<class 'datetime.date'>
>>> time
<class 'datetime.time'>

import datetime as dt
dt.datetime()
'''
