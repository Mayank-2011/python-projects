import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do yu want to travel to? Type the dae in YYYY-MM-DD format: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

song_tags = soup.select('li h3')
songs = []
for song in song_tags:
    songs.append(song.getText().split("\n\n\t\n\t\n\t\t\n\t\t\t\t\t"))
songs = songs[:100]
top_songs = []
for song in songs:
    top_songs.append(song[1].split("\t\t\n\t\n")[0])

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="your spotify client id",
        client_secret="your spotify client secret",
        show_dialog=True,
        cache_path='token.txt',
        username="your spotify display name"
    )
)
user_id = sp.current_user()['id']
song_uris = []
year = date.split("-")[0]
for song in top_songs:
    result = sp.search(q=f"{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)
playlist = sp.user_playlist_create(user = user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
