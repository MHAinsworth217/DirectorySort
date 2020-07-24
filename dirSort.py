# import relevant pyhton modules
import os
import re

# set the default folder to the folder that needs sorted
folder = ("C:\\Users\\mhain\\Downloads")
# convert the contents of the folder into a list
files = os.listdir(folder)

# check to see if the folders that the files are to be sorted into exist
# if not, make them
if not os.path.exists("C:\\Users\\mhain\\Downloads\\executables"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\executables")
if not os.path.exists("C:\\Users\\mhain\\Downloads\\compressed_files"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\compressed_files")
if not os.path.exists("C:\\Users\\mhain\\Downloads\\image_files"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\image_files")
if not os.path.exists("C:\\Users\\mhain\\Downloads\\video_files"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\video_files")
if not os.path.exists("C:\\Users\\mhain\\Downloads\\audio_files"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\audio_files")
if not os.path.exists("C:\\Users\\mhain\\Downloads\\other_files_and_folders"):
    os.mkdir("C:\\Users\\mhain\\Downloads\\other_files_and_folders")

# go through each file individually
for i in files:
    # use regex to match the file type, ignoring case
    execute = re.match(r"\S+\.(exe)", i, re.IGNORECASE)
    comp = re.match(r"\S+\.(zip|rar|tar.gz|tar)", i, re.IGNORECASE)
    img = re.match(r"\S+\.(jpg|jpeg|gif|png|bmp)", i, re.IGNORECASE)
    vid = re.match(r"\S+\.(mp4|wmv|mov|flv|avi|mkv)", i, re.IGNORECASE)
    aud = re.match(r"\S+\.(mp3|m4a|wav)", i, re.IGNORECASE)
    path = os.path.join(folder, i)

    # if statement to sort the files to the correct folders
    if img:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\image_files\\{}".format(i))
        print("Sent {0} to the image_files folder".format(i))
    elif vid:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\video_files\\{}".format(i))
        print("Sent {0} to the video_files folder".format(i))
    elif execute:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\executables\\{}".format(i))
        print("Sent {0} to the executable_files folder".format(i))
    elif comp:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\compressed_files\\{}".format(i))
        print("Sent {0} to the compressed_files folder".format(i))
    elif aud:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\audio_files\\{}".format(i))
        print("Sent {0} to the audio_files folder".format(i))
    else:
        os.rename(path, "C:\\Users\\mhain\\Downloads\\other_files_and_folders\\{}".format(i))
        print("Sent {0} to the audio_files folder".format(i))
