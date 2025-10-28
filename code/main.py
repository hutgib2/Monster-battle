from settings import *
from support import *
from timer import Timer
from monster import Monster, Opponent
from random import randint
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assests()
        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monster_list = ['Sparchu', 'Cleaf', 'Jacana']
        self.player_monsters = [Monster(name, self.back_surfs[name]) for name in player_monster_list]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)

        self.monster_names = list(self.front_surfs.keys())
        self.random_name = self.monster_names[randint(0, len(self.monster_names)-1)]
        self.opponent = Opponent(self.random_name, self.front_surfs[self.random_name], self.all_sprites)
        # ui
        self.ui = UI(self.monster)

    def import_assests(self):
        self.back_surfs = folder_importer('images', 'back')
        self.bg_surfs = folder_importer('images', 'other')
        self.front_surfs = folder_importer('images', 'front')

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfs['floor'].get_frect(center = sprite.rect.midbottom + pygame.Vector2(0, -10))
            self.display_surface.blit(self.bg_surfs['floor'], floor_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(dt)
            self.ui.update()
            # draw 
            self.display_surface.blit(self.bg_surfs['bg'], (0,0))
            self.draw_monster_floor()
            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()