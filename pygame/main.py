from numpy import place
import pygame
import sys
from object import *
import random 

class Music:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('pygame\\res\\theme.mp3')
        pygame.mixer.music.play(loops=True)

class Logic:
    def __init__(self, screen, speed):
        self.player = Player(screen)
        self.platform = Platform(screen)
        self.screen = screen
        self.speed = speed
        self.game_over = False
        self.retry_button = self.get_retry_button()
        self.retry_button_rect = False
        self.score = 0
        self.count_score = True
        # self.music = Music()
        
    def on_update(self):
        if(self.game_over):
            self.render_game_over()
            return
        self.player.render()
        self.rener_platforms()
        self.move_platforms()
        self.try_destroy_platform()
        self.try_create_platform()
        self.count()
        self.check_game_over()
        
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
        max_y = 450
        min_bias_X = 180
        max_bias_X = 200
        new_platform.posY = random.uniform(min_y, max_y)
        new_platform.posX = ObjectEngine.all_objects[-2].posX + random.uniform(min_bias_X, max_bias_X)
        return new_platform

    def count(self):
        if self.player.is_grounded:
            if self.count_score:
                self.score += 1
                self.count_score = False
        else:
            self.count_score = True
        
        font_c = pygame.font.SysFont("Arial", 20)
        score_text = font_c.render(str(self.score), True, (255,255,255))
        self.screen.blit(score_text, (0, 0))
        
       
            
    def check_game_over(self): 
        if self.player.posY >= 600:
            self.game_over = True 
            ObjectEngine.clear_all_objects()
            
    def render_game_over(self):
        self.check_game_over()        
        self.retry_button_rect = self.render_button()
    
    def render_button(self):
        w = self.retry_button.get_width() / 2
        h = self.retry_button.get_height() / 2
        return self.screen.blit(self.retry_button, (400 - w, 300 - h))
        
    def get_retry_button(self):
        font = pygame.font.SysFont("Arial", 50)
        return font.render("Заново", True, (255,255,255))
            
def start_game(screen):
    return Logic(screen, 2.5)        
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    logic = start_game(screen)
    pygame.display.set_caption('Square')
    background_color = (0, 0, 0)
    run = True
    clock = pygame.time.Clock()
    #b1 = Logic.buttons(screen, (400, 300), "Продолжить игру")
    #b2 = Logic.buttons(screen, (500, 300), "Начать заново")
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    logic.player.jump()
                    logic.player.jump_button_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    logic.player.jump_button_pressed = False
                    logic.player.in_jump = False
            if event.type == pygame.MOUSEBUTTONDOWN and logic.retry_button_rect:
                x, y = event.pos
                if logic.retry_button_rect.collidepoint(x ,y):
                    logic = start_game(screen)
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
        screen.fill(background_color)

        logic.on_update()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
