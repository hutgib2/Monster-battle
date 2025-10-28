from settings import *

class UI:
    def __init__(self, monster, player_monsters, simple_surfs):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 60)
        self.left = WINDOW_WIDTH / 2 - 200
        self.top = WINDOW_HEIGHT / 2 + 100
        self.monster = monster
        self.simple_surfs = simple_surfs
        # control
        self.general_options = ['attack', 'heal', 'switch', 'escape']
        self.general_index = {'col': 0, 'row': 0}
        self.attack_index = {'col': 0, 'row': 0}
        self.state ='general'
        self.rows, self.cols = 2,2
        self.player_monsters = player_monsters
        self.visible_monsters = 4
        self.available_monsters = [monster for monster in self.player_monsters if monster != self.monster and monster.health > 0]
        self.switch_index = 0

    def get_input(self, index, keys):
        index['row'] = (index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % self.rows
        index['col'] = (index['col'] + int(keys[pygame.K_d]) - int(keys[pygame.K_a])) % self.cols
        if keys[pygame.K_SPACE]:
            self.state = self.general_options[index['col'] + index['row'] * 2]

    def input(self):
        keys = pygame.key.get_just_pressed()
        if self.state == 'general':
            self.get_input(self.general_index, keys)

        elif self.state == 'attack':
            self.get_input(self.attack_index, keys)

        elif self.state == 'switch':
            self.switch_index = (self.switch_index + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.available_monsters)

    def quad_select(self, index, options):
        rect = pygame.FRect(self.left + 80, self.top + 120, 800, 400)
        pygame.draw.rect(self.display_surface, COLORS['white'],rect, 0, 8)
        pygame.draw.rect(self.display_surface, COLORS['gray'],rect, 8, 8)
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + rect.width / (self.cols * 2) + (rect.width / self.cols) * col
                y = rect.top + rect.height / (self.rows * 2) + (rect.height / self.rows) * row
                i = col + 2 * row
                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']
                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center = (x,y))
                self.display_surface.blit(text_surf, text_rect)

    def switch(self):
        rect = pygame.FRect(self.left + 80, self.top - 200, 800, 400)
        pygame.draw.rect(self.display_surface, COLORS['white'],rect, 0, 8)
        pygame.draw.rect(self.display_surface, COLORS['gray'],rect, 8, 8)
        # menu
        v_offset = 0 if self.switch_index < self.visible_monsters else -(self.switch_index - self.visible_monsters + 1) * rect.height / self.visible_monsters
        for i in range(len(self.available_monsters)):
            x = rect.centerx
            y = rect.top + rect.height / (self.visible_monsters * 2) + rect.height / self.visible_monsters * i + v_offset
            color = COLORS['gray'] if i == self.switch_index else COLORS['black']
            name = self.available_monsters[i].name
            monster_surf = self.simple_surfs[name]
            text_surf = self.font.render(name, True, color)
            text_rect = text_surf.get_frect(center = (x,y))
            if rect.collidepoint(text_rect.center):
                self.display_surface.blit(text_surf, text_rect)
                self.display_surface.blit(monster_surf, text_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case 'general': self.quad_select(self.general_index, self.general_options)
            case 'attack': self.quad_select(self.attack_index, self.monster.abilities)
            case 'switch': self.switch()