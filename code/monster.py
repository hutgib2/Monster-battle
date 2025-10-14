from settings import *
from random import sample

class Monster(pygame.sprite.Sprite):
    def __init__(self, name, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_frect(bottomleft = (200, WINDOW_HEIGHT))
        self.name = name
        # data
        self.element = MONSTER_DATA[name]['element']
        self.health = self.max_health = MONSTER_DATA[name]['health']
        self.abilities = sample(list(ABILITIES_DATA.keys()),4)

class Opponent(pygame.sprite.Sprite):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topright = (WINDOW_WIDTH - 128, 128))