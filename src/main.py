import attr
from src.dash_components.main import main as run_dash
from src.app import app, spotify_client
from src.spotify.utils import Song

def main(app, spotify):
    run_dash(Song)


if __name__ == "__main__":
    main(app, spotify_client)

