import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your-client-id",
                                               client_secret="your-client-secret",
                                               redirect_uri="same-url-as-in-your-spotify-developer-app",
                                               scope="playlist-read-private"))

SPECIFIC_PLAYLIST_ID = 'web-link-to-your-spotify-playlist'

# Read existing content from songs.txt
with open('name-of-txt-file', 'r') as playlist_file:
    contents = playlist_file.read()

# Search for tracks by the specified artist
results = sp.playlist_tracks(SPECIFIC_PLAYLIST_ID)

# Prepare the new content to be added to the file
new_songs = ""
for idx, item in enumerate(results['items']):
    track = item['track']

    if track is None or track['type'] != 'track':
        continue
    
    if 'name' in track and 'artists' in track:
        artist_names = ", ".join(artist['name'] for artist in track['artists'])
        print(idx, track['name'], "by", artist_names)
        new_songs += f"{track['name']} by {artist_names}\n"
    else:
        continue

# Write new content to the file
open('name-of-txt-file', 'w').close()
with open('name-of-txt-file', 'w') as playlist_file:
    playlist_file.write(new_songs)
