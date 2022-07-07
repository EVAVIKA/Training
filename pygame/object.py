import pygame

class ObjectEngine:
    all_objects = []

    @staticmethod
    def add_object(obj):
        ObjectEngine.all_objects.append(obj)

    @staticmethod
    def clear_all_objects():
        ObjectEngine.all_objects = []

    def check_collision(player, on_collision): 

        if ObjectEngine.check_collision_right(player, player.on_collision_right):
            return False

        def is_collide(platform):
            player_left_bot = {'x': player.posX, 'y': player.posY + player.h}
            player_right_bot = {'x': player.posX +
                                player.w, 'y': player.posY + player.h}

            platform_left_top = {'x': platform.posX, 'y': platform.posY}
            platform_right_top = {'x': platform.posX +
                                  platform.w, 'y': platform.posY}

            return (player_left_bot['y'] >= platform_left_top['y'] and (player_right_bot['x'] >= platform_left_top['x'] and player_left_bot['x'] <= platform_right_top['x']), 
                    player_left_bot['y'] != platform_left_top['y'], 
                    platform_left_top['y'])

            
        
        for platform in ObjectEngine.all_objects:
            is_collide_check = is_collide(platform)
            if is_collide_check[0]:
                on_collision(is_collide_check[1], is_collide_check[2])
                
    def check_collision_right(player, on_collision): 

        def is_collide(platform):
            player_left_bot = {'x': player.posX, 'y': player.posY + player.h}
            player_right_bot = {'x': player.posX +
                                player.w, 'y': player.posY + player.h}

            platform_left_top = {'x': platform.posX, 'y': platform.posY}
            platform_right_top = {'x': platform.posX +
                                  platform.w, 'y': platform.posY}

            return (player_right_bot['y'] > platform_left_top['y'] + 30 and player_right_bot['x'] >= platform_left_top['x'] and player_left_bot['x'] <= platform_right_top['x'], 
                    player_right_bot['x'] != platform_left_top['x'], 
                    platform_left_top['x'])

            
        
        for platform in ObjectEngine.all_objects:
            is_collide_check = is_collide(platform)
            if is_collide_check[0]:
                on_collision(is_collide_check[1], is_collide_check[2])
            

class GameObject(pygame.Surface): 
    def __init__(self, screen):
        self.posX = 0
        self.posY = 0
        self.w = 0
        self.h = 0
        self.color = (0, 0, 0)
        self.screen = screen
        

    def render(self):
        res = pygame.draw.rect(self.screen, self.color,
                         (self.posX, self.posY, self.w, self.h))
        return res
 
    def destroy(self):
        ObjectEngine.all_objects.remove(self)
    

class Player(GameObject):
    def __init__(self, screen):
        super().__init__(screen)
        self.color = (255, 255, 0)
        self.h = 50
        self.w = 50
        self.posX = 400 - (self.w / 2) - 50
        self.posY = 200

        self.is_grounded = False
        self.g = 10

        self.jump_force = 300
        self.jump_speed = 17 + self.g
        self.in_jump = False
        self.jump_button_pressed = False

    def jump(self): 
        if not self.is_grounded:
            return
        self.in_jump = True
        self.jump_start_posY = self.posY
        self.jump_end = self.jump_start_posY - self.jump_force

    def on_collision(self, isLower, platform_top):
        self.is_grounded = True
        if (isLower):
            self.posY = platform_top - self.h

    def on_collision_right(self, isRighter, platform_left):
        self.posX -= 3.5
    def render(self):
        self.player_sprite = super().render()
        self.is_grounded = False
        ObjectEngine.check_collision(self, self.on_collision)
        if not self.is_grounded:
            self.posY += self.g
        if self.in_jump and self.jump_button_pressed:
            if self.posY <= self.jump_end:
                self.in_jump = False
            self.posY -= self.jump_speed

class Platform(GameObject):
    def __init__(self, screen):
        super().__init__(screen)
        self.color = (255, 255, 255)
        self.h = 2200
        self.w = 50
        self.posX = 400 - (self.w / 2)
        self.posY = 400
        ObjectEngine.add_object(self)
