def get_playlist_tracks(username):
    print('in play_list_Tracks')
    playlists = sp.user_playlists(username)
    tracks = []
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            results = sp.user_playlist(username, playlist['id'], fields='tracks,next')['tracks']
            tracks.extend(results)
            i = 0
            while results['next']:
                print('in play_list_Tracks')
                tracks.extend(sp.next(results))
                i = i + 1
                print(i)
    print("done")
    return tracks