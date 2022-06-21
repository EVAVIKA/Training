from numpy import place
import pygame
import sys
from object import *
import random 

class Logic:
    def __init__(self, screen, speed):
        self.player = Player(screen)
        self.platform = Platform(screen)
        self.screen = screen
        self.speed = speed
        
    def on_update(self):
        self.player.render()
        self.rener_platforms()
        self.move_platforms()
        self.try_destroy_platform()
        self.try_create_platform()

    def rener_platforms(self):
        for platform in ObjectEngine.all_objects:
            platform.render()

    def move_platforms(self):
        for platform in ObjectEngine.all_objects:
            platform.posX -= self.speed

    def try_destroy_platform(self):
        try:
            platform = ObjectEngine.all_objects[0]
            if platform.posX <= -platform.w:
                platform.destroy()
        except:
            return

    def try_create_platform(self):
        while len(ObjectEngine.all_objects) < 9:
            self.generate_platform()

    def generate_platform(self):
        new_platform = Platform(self.screen)
        min_y = 250
        max_y = 500
        min_bias_X = 100
        max_bias_X = 150
        new_platform.posY = random.uniform(min_y, max_y)
        new_platform.posX = ObjectEngine.all_objects[-2].posX + random.uniform(min_bias_X, max_bias_X)
        return new_platform

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    logic = Logic(screen, 1)
    pygame.display.set_caption('Square')
    background_color = (0, 0, 0)
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    logic.player.jump()
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
        screen.fill(background_color)

        logic.on_update()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
