import sys
import spotipy
import spotipy.util as util
import pprint

def simple_auth_token(username):
    scope = 'user-library-read'

    if not username:
        print ("Usage: python 'file_name' username")
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if not token:
        print ("Can't get token for", username)
    return token
