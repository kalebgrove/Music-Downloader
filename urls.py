import os
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with your YouTube Data API key
API_KEY = 'api-key'

# Function to get YouTube video URL from a search query
def get_youtube_url(query, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    try:
        # Search for the query on YouTube
        request = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=1,
            type='video'
        )
        response = request.execute()
        
        # Extract the video ID and construct the URL
        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return None
    except HttpError as e:
        if e.resp.status == 403:
            print("Quota exceeded. Please wait and try again later.")
            time.sleep(10)  # Wait for 10 seconds before retrying
            return None
        else:
            raise

# Function to read song names from a text file and get their YouTube URLs
def get_urls_from_file(filename, api_key):
    urls = []
    with open(filename, 'r') as file:
        for line in file:
            song_name = line.strip()
            url = get_youtube_url(song_name, api_key)
            if url:
                urls.append(url)
    return urls

# Main code
if __name__ == '__main__':
    song_file = 'name-of-txt-file-with-song-names'  # Your text file with song names
    urls = get_urls_from_file(song_file, API_KEY)
    
    # Write the results to a file
    with open('name-of-txt-file-with-urls', 'w') as playlist_file:
        for url in urls:
            playlist_file.write(url + '\n')
