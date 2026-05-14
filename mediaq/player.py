
import json

from collections import deque
from queue import PriorityQueue
from datetime import datetime

from models import Track
from doubly_linked_list import DoublyLinkedList


class MediaPlayer:

    def __init__(self):

        self.library = {}

        self.playlist = DoublyLinkedList()

        self.up_next = deque()

        self.history = deque(maxlen=20)

    def load_library(self, arquivo):

        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for item in dados:

            track = Track(
                item["id"],
                item["titulo"],
                item["artista"],
                item["duracao"],
                item["rating"],
                item["data_adicao"]
            )

            self.library[track.id] = track

    def add_to_playlist(self, track_id):

        track = self.library.get(track_id)

        if track:
            self.playlist.add(track)

    def play(self):

        track = self.playlist.current()

        if track:

            print(
                f'>>> Tocando: "{track.titulo}" — '
                f'{track.artista} ({track.format_duration()})'
            )

            self.history.appendleft({
                "track": track,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

    def enqueue(self, track_id):

        track = self.library.get(track_id)

        if track:
            self.up_next.append(track)

    def next_track(self):

        if self.up_next:
            track = self.up_next.popleft()

        else:
            track = self.playlist.move_next()

        if track:

            print(
                f'>>> Tocando: "{track.titulo}" — '
                f'{track.artista} ({track.format_duration()})'
            )

            self.history.appendleft({
                "track": track,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

    def get_playlist_state(self):
        """Retorna a playlist e a faixa atual para o CLI exibir."""
        # Retorna uma tupla com a lista e a faixa que está no cursor
        return self.playlist, self.playlist.current()