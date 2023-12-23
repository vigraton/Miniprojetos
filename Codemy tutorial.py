import pygame

# Set up stuff
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Code.com Pygame Tutorial')
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen color
    screen.fill("yellow")

    # Render my game here
    pygame.draw.circle(screen, "#F40179", player_pos, 40)

    # Move circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt

    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt


    if pygame.mouse.get_pressed()[0]:
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]


        # Flip the display to output out work to the screen
    pygame.display.flip()


    # Set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    dt = clock.tick(60) / 1000



pygame.quit()