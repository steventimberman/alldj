import attr


# Songs ##########################################

@attr.s
class Song(object):
    name = attr.ib()
    popularity = attr.ib()
    album = attr.ib()
    length = attr.ib()
    url = attr.ib()
    uri = attr.ib()
    artist = attr.ib()
    artists = attr.ib(factory=list)

def initialize_song(response):
    artists_all = [artist["name"] for artist in response.get("artists", {"name": None})]
    artist_main = artists_all[0]
    return Song(
        name = response.get("name", None),
        popularity = response.get("popularity", None), #1-100 current pop
        album = response.get("album", {"name": None})["name"],
        length = (response.get("duration_ms", 0)) * (10**(-3)), # seconds
        url = response.get("external_urls", None).get("spotify", None),
        uri = response.get("uri", None),
        artist = artist_main,
        artists = artists_all
    )

# Features #########################################

@attr.s
class SongFeatures(object):
    danceability = attr.ib()
    energy = attr.ib()
    key = attr.ib()
    loudness = attr.ib()
    speechiness = attr.ib()
    instrumentalness = attr.ib()
    tempo = attr.ib()
    mode = attr.ib()
    happiness = attr.ib()

def initialize_song_features(response):
    return SongFeatures(
        danceability = response.get("danceability", None),
        energy = response.get("energy", None),
        key = response.get("key", None),
        loudness = response.get("loudness", None),
        speechiness = response.get("speechiness", None),
        instrumentalness = response.get("instrumentalness", None),
        tempo = response.get("tempo", None),
        mode = response.get("mode", None),
        happiness = response.get("valence", None)
    )
