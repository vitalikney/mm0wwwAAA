import random
from Permanents import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, start_x, start_y, width, height):
        super().__init__(group)
        self.life = 1
        self.count_update = 0  # Animation update counter and  action update counter
        self.image = RedStormTrooperNoFire
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 900)
        self.rect.y = 360

    def render(self, *args):  # Test if a point is inside a rectangle
        if args[0] and self.rect.collidepoint((args[1][0] + 20, args[1][1] + 20)):
            self.life = 0

    def update(self, *args):
        if self.life == 0:
            self.kill()
            return
        if len(args) != 0:
            Enemy.render(self, *args)
        if self.count_update == 15:
            fire_sound.set_volume(0.4)
            fire_sound.play()
            Variables.hp -= 9
            self.image = RedStormTrooperFire
        elif self.count_update == 0:
            self.image = RedStormTrooperNoFire
        if self.count_update + 1 > 50:
            self.count_update = -1
        self.count_update += 1


class TieFight(pygame.sprite.Sprite):
    def __init__(self, group, start_x, start_y, width, height):
        super().__init__(group)
        self.life = 1
        self.count_update = 0  # Animation update counter and  action update counter
        self.image = Tf
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, 700)
        self.rect.y = random.randrange(100, 400)

    def render(self, *args):  # Test if a point is inside a rectangle
        if args[0] and self.rect.collidepoint((args[1][0] + 20, args[1][1] + 20)):
            self.life = 0

    def update(self, *args):
        if self.image == ResD:
            self.kill()
            return
        if len(args) != 0:
            TieFight.render(self, *args)
        if self.life == 0:
            self.image = ResD
        if self.count_update == 15:
            fire_sound.set_volume(0.4)
            fire_sound.play()
            Variables.hp -= 10
            self.image = Tf1
        elif self.count_update == 0:
            self.image = Tf
        if self.count_update + 1 > 50:
            self.count_update = -1
        self.count_update += 1
