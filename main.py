import pygame
import math

pygame.init()

#display setup
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("STIMULATION")

icon = pygame.transform.scale(pygame.image.load("./asteroid.png"), (35, 35))
pygame.display.set_icon(icon)

pygame.mixer.music.load("./blast.mp3")

#constants
PLANET_MASS = 100
SHIP_MASS = 5
G = 5# gravitational constant
FPS = 60
PLANET_SIZE = 60#radius
OBJ_SIZE = 10
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("./background.png"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("./planet.png").convert_alpha(), (PLANET_SIZE * 2, PLANET_SIZE * 2))
SHIP =  pygame.transform.scale(pygame.image.load("./asteroid.png").convert_alpha(), (20, 20))

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

class Planets:
    def __init__(self,x,y,mass) -> None:
        self.x = x
        self.y = y
        self.mass = mass
        
    def draw(self):
        win.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))


class SpaceCraft:
    def __init__(self,x,y,vel_x,vel_y, mass) -> None:
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        
    def draw(self):                   #we dont want error rendering floats
        win.blit(SHIP,(int(self.x - OBJ_SIZE), int(self.y - OBJ_SIZE)))
        #pygame.draw.circle(win , RED, (int(self.x), int(self.y)), OBJ_SIZE)
       
    def move(self,planet=None):
        r = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass * planet.mass) / r**2
        acc = force / self.mass
        theta = math.atan2(planet.y - self.y, planet.x - self.x)#atan2 is tan inv of theta
        #                    should be negative
        acc_x = acc * math.cos(theta)
        acc_y = acc * math.sin(theta)
        
        self.vel_x += acc_x
        self.vel_y += acc_y
        
        
        self.x += self.vel_x
        self.y += self.vel_y

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse       
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = SpaceCraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def main():
    running = True
    clock = pygame.time.Clock()
    
    objects = []
    temp_obj_pos = []
    
    planet = Planets(WIDTH//2, HEIGHT//2, PLANET_MASS)
    
    while running:    
        clock.tick(FPS)
        
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos: 
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos
                
 

        #temp_obj_pos -> mouseclicked pos
        win.blit(BG, (0,0))
        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            win.blit(SHIP,(int(temp_obj_pos[0] - OBJ_SIZE), int(temp_obj_pos[1] - OBJ_SIZE)))
            #pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)
        
        for obj in objects.copy():
            obj.draw()
            obj.move(planet=planet)
            off_screen = obj.x < 0 or obj.y > HEIGHT or obj.x > WIDTH or obj.y < 0
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= PLANET_SIZE
            if off_screen :
                objects.remove(obj)
            if collided:
                objects.remove(obj)
                pygame.mixer.music.play()
               
        planet.draw()
            
        pygame.display.update()
    
    pygame.quit()




if __name__ == "__main__":
    main()






