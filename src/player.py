import pygame
from settings import Settings



class Player:
    def  __init__(self):
        self.settings = Settings()

        try:
            #load spaceship image
            self.image = pygame.image.load("../images/spaceship.png")
            self.image = pygame.transform.scale(
                self.image, (self.settings.PLAYER_WIDTH,self.settings.PLAYER_HEIGHT)
            )
        except :

            # if image fails to load
            self.image = pygame.Surface((self.settings.PLAYER_WIDTH, self.settings.PLAYER_HEIGHT))
            self.image.fill((0, 255, 0))

            # prototype : polygon(surface, color, points) -> Rect

            pygame.draw.polygon(self.image,(0,0,0),[
                (0,self.settings.PLAYER_HEIGHT),
                (self.settings.PLAYER_WIDTH//2, 0),
                (self.settings.PLAYER_WIDTH, self.settings.PLAYER_HEIGHT)
            ])
            pass


    def reset_position(self):
        pass

    def update(self):
        pass
    def draw(self):
        pass
        