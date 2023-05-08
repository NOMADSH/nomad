print("ＭＡＤＥ ＢＹ ＠ＣＤＸ９９９")
import time
from pytube import YouTube

while True:
    time.sleep(1)
    print("     🇾​​​​​🇴​​​​​🇺​​​​​🇹​​​​​🇺​​​​​🇧​​​​​🇪​​​​​ 🇻​​​​​🇮​​​​​🇩​​​​​🇪​​​​​🇴​​​​​ 🇩​​​​​🇴​​​​​🇼​​​​​🇳​​​​​🇱​​​​​🇴​​​​​🇩​​​​​🇪​​​​​🇷​​​​​")
    
    time.sleep(1)
    print(" > CHOOSE YOUR QUALITY <")
    print("1 > Low Quality")
    print("2 > High Quality")
    quality = input("Enter Your Quality: ")
    if quality == "1":
        url = input("Enter YouTube video link: ")
        yt = YouTube(url)
        ys = yt.streams.get_lowest_resolution()
        video_title = yt.title
        video_filename = f"{video_title}.mp4"
        print(f"Downloading {video_title}...")
        ys.download(output_path="/sdcard/Download/", filename=video_filename)
        print("Download complete!")
    elif quality == "2":
        url = input("Enter YouTube video link: ")
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        video_title = yt.title
        video_filename = f"{video_title}.mp4"
        print(f"Downloading {video_title}...")
        ys.download(output_path="/sdcard/Download/", filename=video_filename)
        print("Download complete !")
        time.sleep(0.9)
        print("Saved To Downloads Folder !")
    else:
        print("           > Please choose Number '1' or '2 < ")
