from player import MediaPlayer


def run():
    player = MediaPlayer()
    while True:
        comando = input("mediaq> ")
        # 1. Verifica se o usuário quer sair do programa
        if comando == "quit":
            break
        # 2. Verifica se o usuário pediu para exibir a playlist
        elif comando == "playlist show":
            playlist, faixa_atual = player.get_playlist_state()
            if len(playlist) == 0:
                print("A playlist está vazia.")
            else:
                # Usamos enumerate para mostrar o número da faixa (1, 2, 3...)
                for i, track in enumerate(playlist, start=1):
                    # Se a faixa for a atual do cursor, colocamos o ">"
                    if track == faixa_atual:
                        marcador = "> "
                    else:
                        marcador = "  "
                    # Exibe no formato exigido: 1. Águas de Março - Elis Regina (3:32)
                    print(f"{marcador}{i}. {track.titulo} — {track.artista} ({track.format_duration()})")
        # 3. Caso o comando não seja nenhum dos anteriores (Tratamento de erro simples)
        else:
            if comando.strip() != "":  # Ignora se o usuário apenas apertar Enter
                print(f"Erro: Comando desconhecido '{comando}'. Digite 'help' para ver as opções.")