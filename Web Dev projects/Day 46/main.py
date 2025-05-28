from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Get date input and extract year
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# Billboard scraping
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.5"
}
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.get_text(strip=True) for song in song_names_spans]

# Spotify authentication
SPOTIPY_CLIENT_ID = "370564a544064c4692e2719493652140"
SPOTIPY_CLIENT_SECRET = "d01ad5e7658e49cca483130021a71f1f"
SPOTIPY_REDIRECT_URI = "https://example.com/callback"

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Get current user ID
current_user = sp.current_user()
user_id = current_user["id"]

# Search for songs and collect URIs
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create playlist and add songs
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Billboard Hot 100 for {date}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Successfully created playlist with {len(song_uris)} songs!")