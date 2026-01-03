import os
import shutil

path = input("Enter folder path to organize: ")

files = os.listdir(path)

for file in files:
    if file.endswith(".pdf"):
        folder = os.path.join(path, "PDFs")
    elif file.endswith((".jpg", ".png", ".jpeg")):
        folder = os.path.join(path, "Images")
    elif file.endswith((".mp4", ".mkv")):
        folder = os.path.join(path, "Videos")
    else:
        folder = os.path.join(path, "Others")

    if not os.path.exists(folder):
        os.mkdir(folder)

    shutil.move(os.path.join(path, file), os.path.join(folder, file))

print("Files organized successfully!")
