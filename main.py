import pygame
from src.settings import Settings



pygame.init()

settings = Settings()

screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption("Space Invaders")


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False