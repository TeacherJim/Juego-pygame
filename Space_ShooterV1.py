import pygame, random
LittleMeteorsCuantity = random.randint(0, 25)
SmallMeteorsCuantity = random.randint(0, 15)
RegularMeteorsCuantity = random.randint(0, 15)
CoinsCuantity = random.randint(10, 20)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/other_stuff/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 0

    def changespeed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y = 610
        if self.rect.x > 620:
            self.rect.x = 620
        if self.rect.x < 0:
            self.rect.x = 0

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/other_stuff/laser_colita.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    # Update de la velocidad
    def update(self):
        self.rect.y -= 5

# meteoros regulares
class RegularMeteors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor_assets/meteorGrey_med1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -700
            self.rect.x = random.randrange(SCREEN_WIDTH+700)
# meteoros pequeños
class SmallMeteors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor_assets/meteorGrey_big3.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -700
            self.rect.x = random.randrange(SCREEN_WIDTH+700)
# meteoros bastantes pequeños
class LittleMeteors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor_assets/meteorGrey_big2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -700
            self.rect.x = random.randrange(SCREEN_WIDTH+700)

# Clase de la colocación de Coins
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/other_stuff/vida.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 3
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -1000
            self.rect.x = random.randrange(SCREEN_WIDTH+700)

class Game(object):
    def __init__(self):
        # la variable game_over se coloca en Falso para cuando esté en cierta haga cosas
        self.game_over = False
        self.scores = 0
        self.laser_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.little_meteor_list = pygame.sprite.Group()
        self.small_meteor_list = pygame.sprite.Group()
        self.regular_meteor_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.m_background = pygame.image.load("assets/other_stuff/background.png").convert()
        self.m_background.set_colorkey(BLACK)
        self.background = pygame.image.load("assets/other_stuff/background.png").convert()
        self.axis_y = 0
        # monedas
        for i in range(CoinsCuantity):
            self.coins = Coins()
            self.coins.rect.x = random.randrange(675)
            self.coins.rect.y = random.randrange(1200)
            self.coins_list.add(self.coins)
            self.all_sprites_list.add(self.coins)
        # meteoros bastantes pequeños
        for i in range(LittleMeteorsCuantity):
            self.little_meteors = LittleMeteors()
            self.little_meteors.rect.x = random.randrange(675)
            self.little_meteors.rect.y = random.randrange(510)
            self.little_meteor_list.add(self.little_meteors)
            self.all_sprites_list.add(self.little_meteors)
        # Meteoros pequeños
        for i in range(SmallMeteorsCuantity):
            self.small_meteors = SmallMeteors()
            self.small_meteors.rect.x = random.randrange(675)
            self.small_meteors.rect.y = random.randrange(510)
            self.small_meteor_list.add(self.small_meteors)
            self.all_sprites_list.add(self.small_meteors)
        # Meteoros regulares
        for i in range(RegularMeteorsCuantity):
            self.regular_meteors = RegularMeteors()
            self.regular_meteors.rect.x = random.randrange(675)
            self.regular_meteors.rect.y = random.randrange(510)
            self.small_meteor_list.add(self.regular_meteors)
            self.all_sprites_list.add(self.regular_meteors)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def proccess_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.changespeed(-5)
                if event.key == pygame.K_d:
                    self.player.changespeed(5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.changespeed(5)
                if event.key == pygame.K_d:
                    self.player.changespeed(-5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.laser1 = Laser()
                self.laser1.rect.x = self.player.rect.x + 69
                self.laser1.rect.y = self.player.rect.y

                self.laser2 = Laser()
                self.laser2.rect.x = self.player.rect.x + 22
                self.laser2.rect.y = self.player.rect.y
                self.all_sprites_list.add(self.laser1)
                self.all_sprites_list.add(self.laser2)
                self.laser_list.add(self.laser1, self.laser2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.game_over:
                        self.__init__()

        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()
        self.all_sprites_list.update()
        self.coins_hit_list = pygame.sprite.spritecollide(self.player, self.coins_list, True)
        self.L_player_meteor_hit_list = pygame.sprite.spritecollide(self.player, self.little_meteor_list, True)
        self.S_player_meteor_hit_list = pygame.sprite.spritecollide(self.player, self.small_meteor_list, True)
        self.R_player_meteor_hit_list  = pygame.sprite.spritecollide(self.player, self.regular_meteor_list, True)

        # meteor_hit_list = pygame.sprite.spritecoll
        for self.coins in self.coins_hit_list:
            self.scores += 1
            print(self.scores)
        self.all_sprites_list.update()
            # desaparecer meteoros y Laseres cuando colisionan
        for self.laser2 in self.laser_list:
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser2, self.little_meteor_list, True)
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser2, self.small_meteor_list, True)
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser2, self.regular_meteor_list, True)
            for self.little_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser2)
                self.laser_list.remove(self.laser2)
            for self.small_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser2)
                self.laser_list.remove(self.laser2)
            for self.regular_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser2)
                self.laser_list.remove(self.laser2)
        # lo mismo pero con laser1
        for self.laser1 in self.laser_list:
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser1, self.little_meteor_list, True)
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser1, self.small_meteor_list, True)
            self.meteor_hit_list = pygame.sprite.spritecollide(self.laser1, self.regular_meteor_list, True)
            for self.little_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser1)
                self.laser_list.remove(self.laser1)
            for self.small_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser1)
                self.laser_list.remove(self.laser1)
            for self.regular_meteors in self.meteor_hit_list:
                self.all_sprites_list.remove(self.laser1)
                self.laser_list.remove(self.laser1)
            # detectar cuando un laser se sale de la pantalla y borrarlo
            if self.laser1.rect.y < -10:
                self.all_sprites_list.remove(self.laser1)
                self.laser_list.remove(self.laser1)

            if self.laser2.rect.y < -10:
                self.all_sprites_list.remove(self.laser2)
                self.laser_list.remove(self.laser2)

        # si el player choca con un meteorito se acaba el juego
        if len(self.L_player_meteor_hit_list) == 1:
            self.game_over = True
        elif len(self.S_player_meteor_hit_list) == 1:
            self.game_over = True
        elif len(self.R_player_meteor_hit_list) == 1:
            self.game_over = True

        # si el conteo de meteoros dentro de meteor_list llega a 0 entonces
        if (len(self.little_meteor_list) == 0) and (len(self.small_meteor_list) == 0) \
                and (len(self.regular_meteor_list) == 0):
            # se acaba el juego
            self.game_over = True

    def display_frame(self, screen):
        screen.blit(self.background, [0, 0])
        self.relative_y = self.axis_y % self.m_background.get_rect().height
        screen.blit(self.m_background, [0, self.relative_y - self.m_background.get_rect().height])
        if self.relative_y < SCREEN_HEIGHT:
            screen.blit(self.m_background, [0, self.relative_y])
        self.axis_y += 3
        # que si la función game_over se activa entonces
        if self.game_over:
            # fuente
            font = pygame.font.SysFont("Comic Sans", 25)
            # lo que se va a decir, el texto puess
            text = font.render("Game Over Press R to continue...", True, BLACK)
            # posicionar el juego en pantalla
            center_x = (SCREEN_WIDTH // 2) - (text.get_width()//2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() //2)
            # colocar el texto en pantalla cuando termine
            screen.blit(text, [center_x, center_y])
        # si no se ha acabado el juego que siga con los Sprites
        if not self.game_over:
            self.all_sprites_list.draw(screen)
        pygame.display.flip()
def main():
    pygame.init()
    icon = pygame.image.load("assets/other_stuff/icon.png")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Space Shooter!")
    done = False
    clock = pygame.time.Clock()
    game = Game()
    while not done:
        done = game.proccess_events()
        game.run_logic()
        game.display_frame(screen)

        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
