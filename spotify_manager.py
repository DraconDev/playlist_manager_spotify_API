import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class SpotifyManager:
    def __init__(
        self,
    ):
        super(SpotifyManager, self).__init__()
        self.filepath = "../../_login/_API/spotify/spotify.json"
        with open(self.filepath) as f:
            self.auth = json.load(f)
        self.link = "https://api.spotify.com"
        self.client_id = self.auth["client_id"]
        self.client_secret = self.auth["client_secret"]
        self.user_id = "nadracga"
        self.redirect_url = "http://localhost:8000"
        self.sp = self.auth_user()

    def auth_user(
        self,
    ):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_url,
                # scope="user-library-read",
                scope="playlist-modify-public",
            )
        )
        return sp

    def auth_user2(
        self,
    ):
        sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret,
            )
        )

        return sp

    def search_track(self, query="weezer"):
        found = self.sp.search(q=query, limit=20)
        result = {}
        for idx, track in enumerate(found["tracks"]["items"]):
            result[idx + 1] = track["name"]
        return result

    def search_song_url(self, query="weezer"):
        found = self.sp.search(q=query, limit=20)

        return found

    def artist_song(self, song):
        return self.sp.artist(song)

    def get_playlist_items(self, playlist="37i9dQZF1E4t65xCTFYTB8"):
        found = self.sp.playlist_tracks(playlist_id=playlist, limit=20)
        result = {}
        for idx, track in enumerate(found["tracks"]["items"]):
            result[idx + 1] = track["name"]
        return result

    def next_song(self):
        next_song = self.sp.user(self.user.id).queue()
        return next_song

    def create_playlist(self, title):
        playlist = self.sp.user_playlist_create("nadracga", title)
        return playlist
