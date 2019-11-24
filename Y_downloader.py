from pytube import YouTube
import requests
from bs4 import BeautifulSoup as bs

SAVE_PATH = "/home/harshit/Downloads/Mobile_Data.txt/myplaylist"
playlistURL="https://www.youtube.com/playlist?list=PLDcQfybjJLRgxXPK7cS0y1I9QiH-OqCQT"
mainURL="https://www.youtube.com/"
playPage = requests.get(playlistURL)

soup = bs(playPage.text, 'html.parser')

videolist=soup.findAll('a',attrs={'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link'})
#print(videolist)
for a in videolist:
    #print(a.get('href'))
    vidURL=mainURL+a.get('href')
    try:
        # object creation using YouTube which was imported in the beginning
        yt = YouTube(vidURL)
        yt.streams.first().download(SAVE_PATH)
        print(vidURL)
    except:
        print("Connection Error")
