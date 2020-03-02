from Permanents import *


class Background(pygame.sprite.Sprite):
    def __init__(self, group, name, size):  # Name of file, beginning of cut, len of cut
        super().__init__(group)
        self.image = pygame.transform.scale(load_image(name), (size[0], size[1]))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if self.rect.x + args[0] > 0 or self.rect.x + args[0] < -(self.rect.width - WIDTH):
            return
        self.rect.x += args[0]
