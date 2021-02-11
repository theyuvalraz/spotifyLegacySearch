import spotipy
from spotipy import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="",
                                               scope=""))
fail_list = []


def search_spotify(query):
    track_id = ""

    try:
        results = sp.search(q=query, limit=1)
        for idx, track in enumerate(results['tracks']['items']):
            print(idx, track['id'], track['name'], track['artists'][0]['name'])
            track_id = track['id']

        if track_id == "":
            fail_list.append(query)
    except:
        pass

    return track_id


def get_playlist_track_ids(playlist_id):
    results = sp.playlist(playlist_id)
    track_list = []
    for idx, track in enumerate(results['tracks']['items']):
        track_list.append(track['track']['id'])

    return track_list


def add_track_to_list(playlist_id, song_id):
    sp.playlist_add_items(playlist_id, [song_id])


def log_fail_search():
    with open('failed_search.txt', 'w') as f:
        for item in fail_list:
            try:
                f.write("%s\n" % item)
            except:
                pass
