import pygame 
import sys 

def get_player_obj(screen, posX, posY):
    color = (255, 255, 0)
    h = 50 
    w = 50
    pygame.draw.rect(screen, color, (posX, posY, w, h)) 
    return (posX, posY, w, h)

def get_platform(screen, posX, posY):
    color = (255, 255, 255)
    h = 220
    w = 50
    pygame.draw.rect(screen, color, (posX, posY, w, h))
    return (posX, posY, w, h)

def collision(obj1, obj2):
    Obj1LeftBot = (obj1[0], obj1[1] + obj1[3])
    Obj1RightBot = (obj1[0] + obj1[2], obj1[1] + obj1[3])
    
    Obj2LeftTop = (obj2[0], obj2[1])
    Obj2RightTop = (obj2[0] + obj2[2], obj2[1])
    
    return Obj1LeftBot[1] >= Obj2LeftTop[1] and (Obj1RightBot[0] >= Obj2LeftTop[0] or Obj1LeftBot[0] <= Obj2RightTop[0])
    
    
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Square')
    background_color = (0, 0, 0)
    playePos = (20, 20)
    platformPos = (20, 400)
    gravity = 2
    run = True
    
    clock = pygame.time.Clock()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
    
        
        screen.fill(background_color)
        playePos = get_player_obj(screen, playePos[0], playePos[1])
        platformPos = get_platform(screen, platformPos[0], platformPos[1])
        if not collision(playePos, platformPos): playePos = (playePos[0], playePos[1] + gravity)         
        pygame.display.update()
        clock.tick(60)
        
    
if __name__ == '__main__':
    main()