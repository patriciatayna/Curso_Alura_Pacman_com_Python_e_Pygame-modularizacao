import pygame
import constantes
from cenario import Cenario
from fantasma import Fantasma
from pacman import Pacman

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)

if __name__ == "__main__":
    size = 600 // 30

    pacman = Pacman(size)

    blinky = Fantasma(constantes.VERMELHO, size)
    inky = Fantasma(constantes.CIANO, size)
    clyde = Fantasma(constantes.LARANJA, size)
    pinky = Fantasma(constantes.ROSA, size)

    cenario = Cenario(size, pacman)

    cenario.adicionar_movivel(pacman)

    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)


    while True:
        # Calcular as regras
        pacman.calcular_regras()

        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()

        cenario.calcular_regras()

        # Pintar a tela
        screen.fill(constantes.PRETO)

        cenario.pintar(screen)

        pacman.pintar(screen)

        blinky.pintar(screen)
        inky.pintar(screen)
        clyde.pintar(screen)
        pinky.pintar(screen)

        pygame.display.update()
        pygame.time.delay(100)

        # Captura os eventos
        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)