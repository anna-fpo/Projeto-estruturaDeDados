

from player import MediaPlayer

def run():

    player = MediaPlayer()

    while True:

        comando = input("mediaq> ")

        if comando == "quit":
            break

        print(comando)