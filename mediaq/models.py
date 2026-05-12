

class Track:
    def __init__(self, track_id, titulo, artista, duracao, rating, data_adicao):
        self.id = track_id
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.rating = rating
        self.data_adicao = data_adicao

    def format_duration(self):
        minutos = self.duracao
        segundos = self.duracao % 60
        return f"{minutos}:{segundos:02}"

    def __str__(self):
        return f"{self.titulo} — {self.artista} ({self.format_duration()})"