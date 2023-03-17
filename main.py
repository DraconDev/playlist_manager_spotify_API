import json

from spotify_manager import SpotifyManager
from topsongs import top_songs


def main():

    playlist = "37i9dQZF1E4t65xCTFYTB8"
    test_playlist = "5pAGjSJxuAOgEEE05kkA4s"

    # Top songs
    date = 20150301
    top_songs(date)

    # Spotify Manager
    spot_man = SpotifyManager()
    user = spot_man.sp.me()

    # Songs
    search_track = spot_man.search_track("cake")
    artist_song = spot_man.artist_song("spotify:artist:3jOstUTkEu2JkjvRdBA5Gu")
    song_uri = spot_man.search_song_url("heracles")["tracks"]["items"][0]["uri"]
    # song_url = spot_man.search_song_url("heracles")["tracks"]

    # Playlists
    get_playlist = spot_man.sp.playlist(playlist)
    get_playlist_items = spot_man.sp.playlist_items(playlist)
    get_playlist_tracks = spot_man.sp.playlist_tracks(playlist)

    # modify playlists
    # user_playlist_create = spot_man.create_playlist("test")
    # playlist_add_items = spot_man.sp.playlist_add_items(test_playlist, [song_uri])
    # playlist_add_items = spot_man.sp.playlist_add_items(test_playlist, [song_uri])

    def top_list_oldies():
        with open("songs.json", "r") as f:
            top100 = json.load(f)
        songs = []
        for k, v in top100.items():
            songs.append(spot_man.search_song_url(v)["tracks"]["items"][0]["uri"])
        # print(songs)
        spot_man.sp.playlist_add_items(test_playlist, songs)

    top_list_oldies()

    pass


if __name__ == "__main__":
    main()
