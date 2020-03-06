# Passo 1: Selecionar playlist desejada
# Passo 2: Criar nova playlist
# Passo 3: Copiar musicas

import json
import requests
from info import spotify_user_id, spotify_token
class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    def get_spotify_client(self):
        pass

    def get_spotify_url(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artists%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        uri = songs[0]["uri"]

        return uri

    def create_playlist(self):
        request_body = json.dumps({
            "name": "New Playlist",
            "description": " ",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format()
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json("id")

    def add_songs_to_playlist(self):
        pass
