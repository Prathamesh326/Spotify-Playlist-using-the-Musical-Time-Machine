import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
# from pprint import pprint

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"
ENDPOINT = os.getenv("ENDPOINT")

date = input("which year do you want to travel to? Type the data in this formate YYYY-MM-DD: ")
year = date.split("-")[0]
# print(f"year : {year}")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

songs_list = soup.select("li ul li h3")
song_name = [song.getText().strip() for song in songs_list]
songs_uri = []

auth_manager = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()['id']

for song in song_name:
    result = sp.search(q=f"track: {song} year: {year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)

    except IndexError:
        print(f"{song} doesn't  exist in Spotify. Skipped!")

user_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=user_playlist['id'], items=songs_uri)
