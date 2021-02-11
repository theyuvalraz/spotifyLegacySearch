from file_data_extractor import list_files
from spotify_control import search_spotify, get_playlist_track_ids, add_track_to_list, log_fail_search

if __name__ == '__main__':
    playlist_id_const = "7xOpF1FEb8SikxBWd9VPv7"

    initial_track_list = get_playlist_track_ids(playlist_id_const)
    print(initial_track_list)

    for i in list_files("C:/yuvalTemp/Music/kentaro"):
        search_result = search_spotify(i)
        if search_result != "" and search_result not in initial_track_list:
            add_track_to_list(playlist_id_const, search_result)

    log_fail_search()


