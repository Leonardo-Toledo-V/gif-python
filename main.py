import pygame
import sys
import random
import os
import imageio
ruta_dibujos = "/Users/leonardotoledo/Downloads/Octavo Cuatrimestre/Multimedia y diseño digital/Act2"
ruta_gaviota = os.path.join(ruta_dibujos, "gaviota.png")
fondo = os.path.join(ruta_dibujos, "fondo.png")
pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Gaviotas")
fondo = pygame.image.load(fondo)
fondo = pygame.transform.scale(fondo, (ancho, alto))

color_pantalla = (255, 255, 255)
gaviota = pygame.image.load(ruta_gaviota)
gaviota = pygame.transform.scale(gaviota, (120, 120))
gaviota_rect = gaviota.get_rect()
gaviotas = []
for _ in range(4):
    gaviota_info = {
        'x': random.randint(0, ancho - gaviota_rect.width),
        'y': random.randint(0, alto - gaviota_rect.height),
        'velocidad': 9
    }
    gaviotas.append(gaviota_info)
# Configuración de salida de la animación
output_filename = "gaviotas_volando.gif"
grabar_imagen = imageio.get_writer(output_filename, fps=30)
reloj = pygame.time.Clock()
tiempo = 0  # Tiempo transcurrido
while tiempo < 10:  # Solo exporta los primeros 3 segundos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ventana.fill(color_pantalla)
    ventana.blit(fondo,(0,0))
    for gaviota_info in gaviotas:
        gaviota_info['x'] += gaviota_info['velocidad']
        if gaviota_info['x'] >= ancho:
            gaviota_info['x'] = 0
            gaviota_info['y'] = random.randint(0, ancho - gaviota_rect.width)
            gaviota_info['velocidad'] = 5
        ventana.blit(gaviota, (gaviota_info['x'], gaviota_info['y']))
    pygame.display.flip()
    # Agregar el fotograma actual al escritor de imageio
    grabar_imagen.append_data(pygame.surfarray.array3d(ventana).swapaxes(0, 1))
    tiempo += 1 / 30  # Incrementar el tiempo transcurrido
    reloj.tick(30)
# Cerrar el escritor de imageio
grabar_imagen.close()

pygame.quit()
sys.exit()