import sys
import spotipy
import spotipy.util as util
import pprint
import time

from src.spotify.auth import simple_auth_token
from src.spotify.utils import (
    Song, initialize_song,
    SongFeatures, initialize_song_features
)

class Client:
    def __init__(self, username):
        """ A Spotify client class

        Used to search for songs, get song features

        Arguments:
            username {[type]} -- [description]
        """
        self.spotify = spotipy.Spotify(simple_auth_token(username))

    def songs(self, q, limit=5):
        response = self.spotify.search(
                q,
                limit=limit,
                type='track'
            )
        songs = response['tracks']['items']

        return list(map(initialize_song, songs))

    def song_features(self, songs):
        song_uris = [song.uri for song in songs]

        features = list(map(lambda x: self.spotify.audio_features(tracks=x)[0], song_uris))
        return list(map(initialize_song_features, features))

    def song(self, uri):
        response = self.spotify.track(uri)

        return initialize_song(response)




def main():
    start = time.time()
    sp = Client("steventimberman")
    client_active = time.time()
    songs = sp.songs("Hello", limit=2)
    songs_active = time.time()
    features = sp.song_features(songs)
    features_active = time.time()
    print ("-----------")
    print ([song.name for song in songs])
    print ("-----------")
    print ([ft.happiness for ft in features])
    print ("-----------")

    print (f"Time to client: {client_active-start}")
    print (f"Time to songs: {songs_active-start}")
    print (f"Time to feats: {features_active-start}")

if __name__ == "__main__":
    main()



