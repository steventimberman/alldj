import dash
import dash_bootstrap_components as dbc
from src.spotify.client import Client as SpotifyClient

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.MINTY], suppress_callback_exceptions=True)
server = app.server

spotify_client = SpotifyClient("steventimberman")
