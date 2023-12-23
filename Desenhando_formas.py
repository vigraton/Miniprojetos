import pygame

pygame.init()
WINDOW_HEIGHT = 800
WINDOW_WIDHT = 500
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDHT))
pygame.display.set_caption('Desenhando formas!')
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("light blue")

    # ENTENDENDO COORDENADAS:
    # Lado superior esquerdo = 0,0
    # Ao mover para a direita X aumenta, ao ir para baixo Y aumenta

    # 1. Desenhando uma linha (screen, cor, iniciando ponto (x, y), grossura)
    # 2. Desenhando um círculo (screen, cor, centro(x,y), raio, grossura: 0 = fill)
    # 3. Desenhando um retângulo (screen, cor, (top-left x, top-left y, widht, height)

    pygame.draw.line(screen, "purple", (0,50), (800, 50), 20)
    pygame.draw.circle(screen, "blue", (WINDOW_HEIGHT/2, WINDOW_WIDHT/2), 50, 10)
    pygame.draw.rect(screen, "orange", (100, 400, 100, 50))

    pygame.display.flip()

    dt = clock.tick(60)/1000