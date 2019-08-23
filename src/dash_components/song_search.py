import attr

import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from src.app import app
from src.app import spotify_client

from src.dash_components.wrappers import (
    center_wraper,
    center_wraper_two_bodies,
    center_item
)

NUMBER_OF_SONGS = 3

def search_bar(search_id="search_bar"):

    return dcc.Input(
            id=search_id,
            type="text",
            value=""
        )

def songs_list():
    return dbc.ListGroup(id="songs_list")

def make_list_item(song,unique_id):
    name = song.name
    artist = song.artist
    external_url = song.url
    uri = song.uri
    heading = dbc.ListGroupItemText("{} - {}".format(name, artist))

    return dbc.ListGroupItem(heading,id=unique_id, key=str(uri))

@app.callback(Output('songs_list', 'children'), [Input('search_bar', 'value')])
def list_group(query):
    print ("hello")
    all_songs = []
    try:
        print ("here")
        results = spotify_client.songs(query, limit=NUMBER_OF_SONGS)
    except:
        print ("there")
        return all_songs
    else:
        for i in range(len(results)):
            song = results[i]
            all_songs.append(make_list_item(song, "song_item_{}".format(i)))
        print ("all_songs {all_songs}")
        return all_songs


def create_callback(id_num):
    def respond_to_button(clicks, key, data):
        list_id_number = id_num
        current_data = data
        song = spotify_client.song(key)
        current_data.append(attr.asdict(song))
        return current_data
    return respond_to_button


for i in range(NUMBER_OF_SONGS):
    app.callback(Output("song-table-html-{}".format(i), 'children'),
        [Input("song_item_{}".format(i), "num_clicks") for i in range(NUMBER_OF_SONGS)],
        [State("song_item_{}".format(i), "key"),
        State("song-table", 'data')])(create_callback(i))


