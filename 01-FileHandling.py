# fileStream = open("filehandling.txt")
# data = fileStream.read()
# print(data)
# line = fileStream.readline()
# print(line)
# line = fileStream.readline()
# print(line)
# line = fileStream.readline()
# print(line)
# line = fileStream.readline()
# print(line)
# line = fileStream.readline()
# print(line)
# data = fileStream.read(100)
# print(data)
# fileStream.close()


# fileStream = open("file-handling2.txt", "w")
# fileStream.write("some more data")
# fileStream.close()

# fileStream = open("file-handling2.txt", "a")
# fileStream.write("this data will be appended")
# fileStream.close()


# fileStream = open("watch.jpeg", "rb")
# data = fileStream.read()
# print(data)

# fileStream = open("watch-copy.jpeg", "wb")
# fileStream.write(data)

# fileStream = open("file-handling.txt", "r+")
# data = fileStream.read()
# print(data)
# fileStream.write("\nsome new data added by code")
# fileStream.seek(0)
# data = fileStream.read()
# print("Data after writing something - ", data)

# fileStream = open("file-handling2.txt", "w+")
# fileStream.write("some text...")
# fileStream.seek(0)
# data = fileStream.read()
# print(data)

fileStream = open("file-handling2.txt", "a+")
fileStream.write("some text to be appended...")
fileStream.seek(0)
data = fileStream.read()
print(data)