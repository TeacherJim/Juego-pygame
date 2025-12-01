# importaciones
import pygame, random
# constantes
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (57, 255, 20)
#inicio de Pygame
pygame.init()
icon = pygame.image.load("assets/other_stuff/icon.png")
# El mixer para la musica
pygame.mixer.init()
#creacion de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(icon)
# Titulo
pygame.display.set_caption("SPACE SHOOTER!!")
# Clock de FPS
clock = pygame.time.Clock()
axis_y = 0
def show_go_screen():
    screen.blit(m_background, [0,0])
    draw_text(screen, "Space Shooter!", 65, WIDTH//2, HEIGHT//4)
    draw_text(screen,"Follow me in Ig: eljimese ", 27, WIDTH//2, HEIGHT//2)
    draw_text(screen,"Press any key to start", 20, WIDTH//2, HEIGHT*3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# función para dibujar algo en el juego (almacena los parametros surface, text, etc ,etc)
def draw_text(surface, text, size, x, y):
    # se crea la fuente
    font = pygame.font.SysFont("Comic Sans", size)
    # se renderiza la superficie y el color
    text_surface = font.render(text, True, WHITE)
    # se obtienen las coordenadas del texto
    text_rect = text_surface.get_rect()
    # se colocan en el medio y el tope de x and y
    text_rect.midtop = (x, y)
    # se coloca el texto en pantalla con las coordenadas
    surface.blit(text_surface, text_rect)
# función barra de salud con los parametros asignados
def draw_health_bar(surface, x, y, percentage):
    # se define constantes
    BAR_LENGTH = 100
    BAR_HEIGHT = 15
    # se define el tamaño del relleno con el resultado
    fill = (percentage / 100) * BAR_LENGTH
    # se define los paremetros del borde
    border = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    # se define los parametros del relleno
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    # se dibujan el borde y el relleno con sus parametros
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, border, 3)
# funcion para crear meteoros
def CreateMeteor():
    # se iguala la variable con la clase
    meteor = Meteor()
    # se añade la variable (Cada metero) a las listas
    all_sprites.add(meteor)
    meteor_list.add(meteor)
# Clase Jugador
class life(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #cargamos la imagen
        self.image = pygame.image.load("assets/other_stuff/vida.png").convert()
        # Eliminamos el fondo negro del PNG
        self.image.set_colorkey(BLACK)
        # Obtenemos las cordenadas de nuestra imagen
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-600, -500)
        self.speed_y = 3

    def update(self):
        self.rect.y += 3
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-600, -500)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #cargamos la imagen
        self.image = pygame.image.load("assets/other_stuff/player.png").convert()
        # Eliminamos el fondo negro del PNG
        self.image.set_colorkey(BLACK)
        # Obtenemos las cordenadas de nuestra imagen
        self.rect = self.image.get_rect()
        # colocamos esta imagen
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        # velocidad 0
        self.speed_x = 0
        # la vida 0
        self.shield = 100
    # El update de nuestro jugador
    def update(self):
        self.speed_x = 0
        # obtenemos el estado de las teclas presionadas
        keyState = pygame.key.get_pressed()
        # configuramos controles
        if keyState [pygame.K_LEFT] or keyState [pygame.K_a]:
            self.speed_x -= 10
        if keyState [pygame.K_RIGHT] or keyState [pygame.K_d]:
            self.speed_x += 10
        # igualamos las cordenadas de nuestro jugador a su velocidad
        self.rect.x += self.speed_x
        # colocamos los limites
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    # función shoot
    def shoot(self):
        # la variable se iguala a la clase Bullet creada (imagen)
        bullet = Bullet(self.rect.centerx, self.rect. top - 15 )
        bullet2 = Bullet(self.rect.x + 27, self.rect.top)
        bullet3 = Bullet(self.rect.x + 76, self.rect. top)
        # se agrega a las listas
        all_sprites.add(bullet, bullet2, bullet3)
        bullets.add(bullet, bullet2, bullet3)
# Clase meteoro
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Colocamos imagenes de la variable y se elige con choice
        self.image = random.choice(meteor_images)
        # Eliminamos el fondo
        self.image.set_colorkey(BLACK)
        # Obtenemos coordenadas
        self.rect = self.image.get_rect()
        # colocamos las cordenadas con Random
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-1000, -500)
        # configuramos su velocidad con Random
        self.speed_y = random.randrange(1, 10)
        self.speed_x = random.randrange(-5, 5)
    # metodo update
    def update(self):
        # igualamos las coordenadas a su respectiva velocidad
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        # si se sale de la pantalla restauramos sus valores con Random
        if self.rect.top > HEIGHT + 200 or self.rect.left < -200 or self.rect.right > WIDTH + 200:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-1000, -500)
            self.speed_y = random.randrange(1, 10)
            self.speed_x = random.randrange(-5, 5)
# clase Kufo
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_anim[0]
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.speed_x = 10
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1

    def update(self):
        self.rect.x += self.speed_x
        now = pygame.time.get_ticks()
        if self.rect.y > 180:
            all_sprites.remove(alien)
            aliens.remove(alien)
        if self.rect.x == WIDTH-50 or self.rect.x == 0:
            self.speed_x *= -1
            self.rect.y += 25
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 0.2
            if self.frame == len(alien_anim):
                self.frame = 0
                #self.kill()
            else:
                center = self.rect.center
                self.image = alien_anim[int(self.frame)]
                self.rect = self.image.get_rect()
                self.rect.center = center
# clase Bullet
class Bullet(pygame.sprite.Sprite):
    # se hace la función de auto inicio con los parametros x and y
    def __init__(self, x, y):
        super().__init__()
        # colocamos imagen
        self.image = pygame.image.load("assets/other_stuff/laser_colita.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        # velocidad de la bala
        self.speed_y = -10
    # metodo update
    def update(self):
        self.rect.y += self.speed_y
        # si la bala pasa a -10 desaparece
        if self.rect.bottom < -10:
            self.kill()
# animación de de explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
# listas de imagenes
meteor_images = []
# lista de los meteoros
meteor_list = ["assets/meteor_assets/meteorGrey_big1.png", "assets/meteor_assets/meteorGrey_big2.png",
                "assets/meteor_assets/meteorGrey_big3.png", "assets/meteor_assets/meteorGrey_big4.png",
				"assets/meteor_assets/meteorGrey_med1.png", "assets/meteor_assets/meteorGrey_med2.png",
                "assets/meteor_assets/meteorGrey_small1.png", "assets/meteor_assets/meteorGrey_small2.png",
				"assets/meteor_assets/meteorGrey_tiny1.png", "assets/meteor_assets/meteorGrey_tiny2.png"]
# por cada imagen en meteor_list
for img in meteor_list:
    # se le agrega img imagen meteor_images con el metodo convert
    meteor_images.append(pygame.image.load(img).convert())
# animacion de explosiones
explosion_anim = []
for i in range(9):
	file = "assets/explosion_assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)
# animacion de alien
alien_anim = []
for i in range(9):
	file = "assets/k_ufo_assets/k_ufo_0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	#img_scale = pygame.transform.scale(img, (70, 70))
	alien_anim.append(img)
# fondo de la ventana
m_background = pygame.image.load("assets/other_stuff/background.png").convert()
axis_y = 0
# sonidos
laser_sound = pygame.mixer.Sound("assets/sounds/assets_laser5.ogg")
explosion_sound = pygame.mixer.Sound("assets/sounds/assets_explosion.wav")
# musica de fondo
pygame.mixer.music.load("assets/sounds/music_background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# El trigger del bucle
running = True
game_over = True
# El bucle principal
while running:
    if game_over:

        game_over = False
        # se hace la lista de todos los Sprites
        all_sprites = pygame.sprite.Group()
        # se hace la lista de todos los meteoros
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        aliens = pygame.sprite.Group()
        LifeBoost = pygame.sprite.Group()
        # agregamos la clase Player a la variable
        player = Player()
        # agregamos la variable a la lista de todos los Sprites
        all_sprites.add(player)
        # creamos nuestros meteoros
        for i in range(600):
            CreateMeteor()
        # ocultar mouse
        pygame.mouse.set_visible(0)
        alien = Alien()
        aliens.add(alien)
        life_boost = life()
        score = 0
        show_go_screen()
    # el control de los FPS
    clock.tick(60)
    # detecta los eventos
    for event in pygame.event.get():
        # si el evento es igual a QUIT entonces se detiene el bucle
        if event.type == pygame.QUIT:
            running = False
        # trigger de los laseres
        elif event.type == pygame.KEYDOWN:
            # si se preciona Space
            if event.key == pygame.K_SPACE:
                laser_sound.play()
                #se inicia la función shoot
                player.shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            laser_sound.play()
            player.shoot()
    # se actualizan los sprites
    all_sprites.update()
    if score == 200 or score == 800:
        all_sprites.add(alien)
    # COLISIONES (LASER --> Alien)
    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    for hit in hits:
        # se agrega +1 punto
        score += 100
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        all_sprites.remove(alien)
        aliens.remove(alien)
        # se reproduce una explosion
        explosion_sound.set_volume(0.2)
        explosion_sound.play()
    # COLISIONES ( LASER --> Meteoro)
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    # por cada colision en hits se hace
    for hit in hits:
        # se agrega +1 punto
        score += 1
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        # se reproduce una explosion
        explosion_sound.set_volume(0.2)
        explosion_sound.play()
        # se crea otro meteoro
        CreateMeteor()
    # checar colisiones del jugador contra el meteoros
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    # por cada colision en hits se hace
    for hit in hits:
        # quitas - 10 de vida
        player.shield -= 10
        # se crea otro meteoro
        CreateMeteor()
        # si se llega la vida a 0 se acaba el juego
        if player.shield <= 0:
            game_over = True
    if player.shield <= 40:
        LifeBoost.add(life_boost)
        all_sprites.add(life_boost)
    hits = pygame.sprite.spritecollide(player, LifeBoost, True)
    # por cada colision en hits se hace
    for hit in hits:
        # sumas 10 de vida
        player.shield += 40
        all_sprites.remove(life_boost)
        LifeBoost.remove(life_boost)
    # el fondo de la ventana
    screen.blit(m_background, (0, 0))
    relative_y = axis_y % m_background.get_rect().height
    screen.blit(m_background,[0, relative_y-m_background.get_rect().height])
    if relative_y < HEIGHT:
        screen.blit(m_background,[0, relative_y])
    axis_y += 3
    # se dibujan los sprites en la ventana
    all_sprites.draw(screen)
    # Marcador
    draw_text(screen, str(score) + " Pts", 35, WIDTH // 2, 10)
    draw_text(screen, "Health", 27, 55, 10)
    # Barra de salud
    draw_health_bar(screen, 100, 25, player.shield)
    # la actualizacion de la ventana
    pygame.display.flip()
# cuando se detenga el bucle sale de la ventana
pygame.quit()

