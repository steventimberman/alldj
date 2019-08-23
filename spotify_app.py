import sys
import spotipy
import spotipy.util as util
import pprint

from spotify.auth import simple_auth_token

from dash_components.song_search import main as dash_main

class SpotifyApp:
    def __init__(self, username):
        self.spotify_client = spotipy.Spotify(simple_auth_token(username))

    def search_songs(self, q, limit=5):
        songs = self.spotify_client.search(
            q,
            limit=limit,
            type='track'
        )['tracks']
        return songs

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = "steventimberman"
    sp = SpotifyApp(username)

    dash_main(sp)

