
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
        """Retorna a faixa atual apontada pelo cursor e adiciona ao histórico."""
        track = self.playlist.current()

        if track:
            # Adiciona ao histórico (deque de tamanho 20) com o timestamp atual
            self.history.appendleft({
                "id": track.id,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            return track
        return None

    def enqueue(self, track_id):
        """Busca uma música na biblioteca e adiciona à fila de reprodução imediata Up Next."""
        track = self.library.get(track_id)
        if track:
            self.up_next.append(track)
            return track
        return None

    def next_track(self):
        """Avança para a próxima música respeitando a precedência da fila Up Next."""
        track = None

        # 1. Tenta pegar da fila Up Next (Precedência máxima)
        if self.up_next:
            track = self.up_next.popleft()
        # 2. Se a fila estiver vazia, avança o cursor da playlist
        else:
            track = self.playlist.move_next()

        # 3. Se encontrou uma música para tocar, joga no histórico
        if track:
            self.history.appendleft({
                "id": track.id,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            return track
        return None

    def get_playlist_state(self):
        """Retorna a playlist e a faixa atual para o CLI exibir."""
        # Retorna uma tupla com a lista e a faixa que está no cursor
        return self.playlist, self.playlist.current()

    def add_to_playlist(self, track_id):
        """Busca uma música na biblioteca e adiciona à playlist atual."""
        track = self.library.get(track_id)
        if track:
            self.playlist.add(track)
            return track
        return None

    def remove_from_playlist(self, position):
        """Remove a música na posição informada (base 1)."""
        return self.playlist.remove_at(position)

    def get_playlist_state(self):
        """Retorna a playlist e a faixa atual para o CLI exibir."""
        return self.playlist, self.playlist.current()

    def new_playlist(self, nome):
        """Reseta a playlist atual criando uma nova instância de DoublyLinkedList."""
        self.playlist = DoublyLinkedList()
        self.playlist_name = nome  # Adicione self.playlist_name = "" no seu __init__
        return nome

    def prev_track(self):
        """Retrocede o cursor para a música anterior na playlist."""
        # Move o cursor da lista duplamente encadeada para trás
        track = self.playlist.move_prev()

        # Se mudou com sucesso para uma música válida, joga no histórico
        if track:
            self.history.appendleft({
                "id": track.id,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            return track

        return None

    def get_queue(self):
        """Retorna a fila Up Next atual."""
        return self.up_next