from settings import *

class UI:
    def __init__(self, monster):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 60)
        self.left = WINDOW_WIDTH / 2 - 200
        self.top = WINDOW_HEIGHT / 2 + 100
        self.monster = monster
        # control
        self.general_options = ['attack', 'heal', 'switch', 'escape']
        self.general_index = {'col': 0, 'row': 0}
        self.attack_index = {'col': 0, 'row': 0}
        self.state ='general'
        self.rows, self.cols = 2,2

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

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case 'general': self.quad_select(self.general_index, self.general_options)
            case 'attack': self.quad_select(self.attack_index, self.monster.abilities)
            case 'switch': self.switch()