from pytube import YouTube, Playlist
play_list = Playlist('https://www.youtube.com/playlist?list=PLD6SPjEPomatGovrtQFb84p3LJtoeUEoS')



for link in play_list:
    print("'" + link + "',")

