import pygame
import time
import os


def Paint():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    # Colores
    Rojo = (255, 0, 0)
    Naranja = (255, 128, 0)
    Amarillo = (255, 255, 0)
    VerdeClaro = (0, 179, 71)
    Verde = (0, 255, 0)
    Cian = (7, 184, 255)
    Azul = (0, 0, 255)
    Lila = (108, 70, 117)
    Blanco = (255, 255, 255)
    Negro = (0, 0, 0)
    Menta = (216, 249, 204)

    # variables generales
    Tamano = (800, 600)
    Radio = 1
    UltimaPosicion = (0, 0)
    Dibujando = False

    Ventana = pygame.display.set_mode(Tamano)
    Ventana.fill(Blanco)
    clock = pygame.time.Clock()
    Letra = pygame.font.SysFont("Arial", 20)
    # Barra superior
    pygame.draw.rect(Ventana, Negro, (0, 0, 800, 50))
    pygame.draw.rect(Ventana, Rojo, (10, 8, 35, 35))
    pygame.draw.rect(Ventana, Naranja, (47, 8, 35, 35))
    pygame.draw.rect(Ventana, Amarillo, (84, 8, 35, 35))
    pygame.draw.rect(Ventana, Verde, (121, 8, 35, 35))
    pygame.draw.rect(Ventana, VerdeClaro, (158, 8, 35, 35))
    pygame.draw.rect(Ventana, Cian, (195, 8, 35, 35))
    pygame.draw.rect(Ventana, Azul, (232, 8, 35, 35))
    pygame.draw.rect(Ventana, Lila, (269, 8, 35, 35))
    pygame.draw.rect(Ventana, Cian, (460, 8, 90, 35))
    Lapiz = Letra.render("LAPIZ", 0, (Negro))
    pygame.draw.rect(Ventana, Menta, (560, 8, 90, 35))
    Pintar = Letra.render("PINTAR", 0, (Negro))
    pygame.draw.rect(Ventana, Blanco, (660, 8, 90, 35))
    Limpiar = Letra.render("LIMPIAR", 0, (Negro))
    pygame.draw.rect(Ventana, Rojo, (760, 8, 35, 35))
    Salir = Letra.render("X", 0, (Negro))

    # Barra lateral
    pygame.draw.rect(Ventana, Negro, (0, 50, 80, 80), width=1)
    pygame.draw.line(Ventana, Negro, [8, 93], [72, 90], width=1)
    pygame.draw.rect(Ventana, Negro, (0, 133, 80, 80), width=1)
    pygame.draw.rect(Ventana, Negro, (10, 143, 60, 60), width=2)
    pygame.draw.rect(Ventana, Negro, (0, 216, 80, 80), width=1)
    pygame.draw.circle(Ventana, Negro, [40, 250], 30, width=2)
    pygame.draw.rect(Ventana, Negro, (0, 299, 80, 20), width=1)
    pygame.draw.line(Ventana, Negro, [8, 309], [72, 309], width=2)
    pygame.draw.rect(Ventana, Negro, (0, 322, 80, 20), width=1)
    pygame.draw.line(Ventana, Negro, [8, 332], [72, 332], width=4)

    # definiciones
    def Dibujo(srf, color, comienzo, final, Radio=1):
        dx = final[0] - comienzo[0]
        dy = final[1] - comienzo[1]
        distancia = max(abs(dx), abs(dy))
        for i in range(distancia):
            x = int(comienzo[0] + float(i) / distancia * dx)
            y = int(comienzo[1] + float(i) / distancia * dy)
            pygame.draw.circle(srf, color, (x, y), Radio)

    try:
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                color = Rojo
                pygame.draw.circle(Ventana, color, e.pos, Radio)
                Dibujando = True
            if e.type == pygame.MOUSEBUTTONUP:
                Dibujando = False
            if e.type == pygame.MOUSEMOTION:
                if Dibujando:
                    pygame.draw.circle(Ventana, color, e.pos, Radio)
                    Dibujo(Ventana, color, e.pos, UltimaPosicion, Radio)
                UltimaPosicion = e.pos
            Ventana.blit(Lapiz, (480, 15))
            Ventana.blit(Pintar, (575, 15))
            Ventana.blit(Limpiar, (670, 15))
            pygame.display.flip
            pygame.display.update()
            clock.tick(60)

    except StopIteration:
        pass
    pygame.quit()


if __name__ == '__main__':
    Paint()
