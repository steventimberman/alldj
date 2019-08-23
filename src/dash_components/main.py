import attr
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src.spotify.utils import Song

from src.app import app
from src.app import spotify_client

from src.dash_components.wrappers import (
    center_wraper,
    center_wraper_two_bodies,
    center_item
)
from src.dash_components.song_search import (
    search_bar,
    songs_list,
    make_list_item
)

from src.dash_components.song_table import SongTable

def main(song):

    song_fields = [field.name for field in attr.fields(song)]
    initial_table_object = SongTable(song_fields)
    data_table = initial_table_object.table

    song_list_length = html.Div(id='song-data', style={'display': 'none'})

    title = dbc.Col([
            center_item(html.H1("Find on Spotify")),

    ])

    body1 = dbc.Col([
            center_item(search_bar()),
            center_item(songs_list())
    ])

    body2 = dbc.Col([
            center_item(data_table)
    ])

    app.layout = html.Div([center_wraper_two_bodies(title, body1,body2)])




    # @app.callback(Output('songs_json_data', 'children'), [Input('search_bar', 'value')])
    # def list_group(query):
    #     song_uris = []
    #     try:
    #         results = spotify.songs(query, limit=3)
    #     except:
    #         return none
    #     return [{i: results[i].uri} for song in range(len(results))]



    # @app.callback(
    #     Output('song-table', 'data'),[
    #     Input('')
    # ])
    # def populate_table():
    #     pass

    # @app.callback(
    # Output('adding-rows-table', 'data'),
    # [Input('editing-rows-button', 'n_clicks')],
    # [State('adding-rows-table', 'data'),
    #  State('adding-rows-table', 'columns')])
    # def add_row(n_clicks, rows, columns):
    #     if n_clicks > 0:
    #         rows.append({c['id']: '' for c in columns})
    #     return rows


    app.run_server(debug=True)
