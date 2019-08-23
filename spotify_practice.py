import sys
import spotipy
import spotipy.util as util
import pprint

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.search("Hello", limit=2, type='track')['tracks']
    pprint.pprint([item.keys() for item in results["items"]])
    # for item in results['items']:
    #     name = item['name']
    #     artist = item['artists'][0]['name']
    #     print (name, artist)
else:
    print ("Can't get token for", username)
