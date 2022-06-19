from turtle import width
import pygame 
import random 

width = 800 
height = 600 
screen = pygame.display.set_mode((width, height))

def get_pipes():
    pipe_height = res[1].get_height()
    offset = height/3 
    y_2 = offset + random.randrange(0, 50)
    pipes_x = width + res[1].get_width()
    y_1 = (pipe_height - y_2 + offset) * -1
    pipe = [{'x': pipes_x, 'y': y_1}, {'x': pipes_x, 'y': y_2}]
    return pipe 
    
    
    
    
    
def main_game():
    score = 0 
    player_x = int(width/10)
    player_y = int(height/2)
    base_x = 0
    
    pipe = get_pipes()
    print(pipe)    

if __name__ == "__main__":
    pygame.init() 
    res = [pygame.image.load('res/player.png'), pygame.image.load('res/obst.png')]
    continue_game = True
    while continue_game:
        main_game() 
    