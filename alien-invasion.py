import sys
import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color= (230, 230, 230)

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("assets/spaceship.png")
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)        
            self.ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    
    ai.run_game()                        