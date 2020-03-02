from Permanents import *
from Variables import *


class DrawMouse(pygame.sprite.Sprite):  # Draw new cursor
    def __init__(self, group):
        super().__init__(group)
        self.image = DrawMouseImage
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 320

    def update(self, *args):
        if args[2] == 0:  # Check if the display is receiving mouse input
            pygame.mouse.set_visible(True)
            self.rect.x = 500
            self.rect.y = 320
        else:
            pygame.mouse.set_visible(False)
            self.rect.x = args[0]
            self.rect.y = args[1]


class FirstPlay(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = FirstPlayNoFire
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 400
        self.count_fire = 0

    def update(self, *args):
        if args[0] != 0 and args[1]:
            self.image = FirstPlayFire
            self.count_fire = 1
        if self.count_fire != 0:
            self.count_fire += 1
        if self.count_fire + 1 > 9:
            self.image = FirstPlayNoFire
            self.count_fire = 0


class DrawPlayer(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = StandPLayer
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 400
        self.count_animation = 0
        self.left = False
        self.right = False

    def render(self, *args):
        if args[0]:
            self.left = False
            self.right = True
        elif args[1]:
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = False
            self.count_animation = 0

    def update(self, *args):
        DrawPlayer.render(self, *args)
        if self.count_animation + 1 > 17:
            self.count_animation = 0
        # print(self.count_animation)
        if self.right:
            self.image = RightPlayer[self.count_animation // 4]
            self.count_animation += 1
        elif self.left:
            self.image = LeftPlayer[self.count_animation // 4]
            self.count_animation += 1
        else:
            self.image = StandPLayer
