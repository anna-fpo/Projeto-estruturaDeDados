from player import MediaPlayer


def run():
    player = MediaPlayer()

    while True:
        entrada = input("mediaq> ").strip()
        if not entrada:
            continue

        partes = entrada.split()

        # 1. SAIR
        if entrada == "quit":
            break

        # 2. CARREGAR BIBLIOTECA
        elif entrada.startswith("library load"):
            try:
                arquivo = partes[2]
                player.load_library(arquivo)
                print(f"Biblioteca carregada: {len(player.library)} faixas.")
            except (IndexError, FileNotFoundError):
                print("Erro: Arquivo não encontrado ou formato inválido.")

        # 3. MOSTRAR PLAYLIST
        elif entrada == "playlist show":
            playlist, faixa_atual = player.get_playlist_state()
            if len(playlist) == 0:
                print("A playlist está vazia.")
            else:
                for i, track in enumerate(playlist, start=1):
                    marcador = "> " if track == faixa_atual else "  "
                    print(f"{marcador}{i}. {track}")

        # 4. CRIAR NOVA PLAYLIST
        elif entrada.startswith("playlist new"):
            try:
                nome_playlist = " ".join(partes[2:])
                if not nome_playlist:
                    print("Erro: Informe um nome para a playlist.")
                else:
                    player.new_playlist(nome_playlist)
                    print(f"Playlist '{nome_playlist}' criada.")
            except IndexError:
                print("Erro: Use o formato 'playlist new <nome>'")

        # 5. ADICIONAR NA PLAYLIST
        elif entrada.startswith("playlist add"):
            try:
                track_id = int(partes[2])
                track = player.add_to_playlist(track_id)
                if track:
                    print(f"Adicionado: {track.titulo}")
                else:
                    print(f"Erro: Música com ID {track_id} não encontrada.")
            except (IndexError, ValueError):
                print("Erro: Use o formato 'playlist add <id_da_musica>'")

        # 6. REMOVER DA PLAYLIST
        elif entrada.startswith("playlist remove"):
            try:
                pos = int(partes[2])
                removida = player.remove_from_playlist(pos)
                if removida:
                    print(f"Removido: {removida.titulo}")
                else:
                    print(f"Erro: Posição {pos} inválida.")
            except (IndexError, ValueError):
                print("Erro: Use o formato 'playlist remove <posicao_na_lista>'")

        # 7. TOCAR (PLAY)
        elif entrada == "play":
            track = player.play()
            if track:
                print(f'>>> Tocando: "{track.titulo}" — {track.artista} ({track.format_duration()})')
            else:
                print("Erro: Nenhuma música na playlist atual ou o cursor está vazio.")

        # 8. COMANDO DESCONHECIDO (Sempre por último!)
        else:
            print(f"Erro: Comando desconhecido '{entrada}'.")