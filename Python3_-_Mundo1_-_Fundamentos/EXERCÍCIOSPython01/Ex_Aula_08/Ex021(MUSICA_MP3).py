# Desafio 021 - Aula 08
# Faça um programa em Python que abra e reproduza o áudio de
# um arquivo MP3.
# ------------------------------------------------------------------------
import pygame
mixer.init()
mixer.music.load('Sweden.mp3')
mixer.music.play()

import time
time.sleep(360)

# Para funcionar deve-se baixar e adicionar "Sweden.mp3" ao mesmo diretório do script Python.