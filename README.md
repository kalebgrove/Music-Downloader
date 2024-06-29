# Music-Downloader
Download your music from one of your playlists from Spotify using yt-dlp.

For the code to work, it's required to have python installed on your computer.
It's necessary to open the Spotify Developer Dashbord and create a new app to obtain the API as well as the secret codes necessary for the code to work correctly.

Each file must be executed one after the other in the following order:
  1. python application2.py
  2. python urls.py
  3. python download.py
  4. python movesongs.py

The first program saves the name of the songs in addition to the artist in a text file. In second place, it's necessary to store the urls of the songs in order for yt-dlp to work correctly.
Thirdly we can download all of the songs that will be stored in the same directory as the code is found in. Lastly, the movesongs.py code allows you to move all .mp4 files to another directory.
