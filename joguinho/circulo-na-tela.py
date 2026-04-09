# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('jogo do gugu')
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


superficie = pygame.Surface((800,400))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

 
    # Tentei dar display na imagem /home/gustavo/ra305836/projetos/joguinho/sprites/pngwing.com.png e não consegui :(
    class Arma(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('/home/gustavo/ra305836/projetos/joguinho/sprites/pngwing.com.png').convert_alpha()
            self.rect = self.image.get_rect(center=(400,300))
    all_sprites = pygame.sprite.Group()
    arma = Arma()
    all_sprites.add(arma)

   # Fiz um buneco (ele é careca)
    corpo_do_boneco = pygame.Rect(0,0,50,100)
    corpo_do_boneco.center = (player_pos)
    pygame.draw.rect(screen,"blue",corpo_do_boneco)
    pygame.draw.circle(screen, "pink", player_pos+pygame.Vector2(0,-70), 40)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()