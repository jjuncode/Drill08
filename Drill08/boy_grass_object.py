from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x,self.y = random.randint(0,300),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1)% 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class BallBig:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x,self.y = random.randint(0,700),599
        self.velocity = random.randint(5,20)
    def update(self):
        if ( self.y > 70 ):
            self.y -=self.velocity
        else:
            self.y = 70

    def draw(self):
        self.image.draw(self.x,self.y)


class BallSmall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x,self.y  =random.randint(0,700),599
        self.velocity = random.randint(5,20)

    def update(self):
        if (self.y > 60):
            self.y -= self.velocity
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global world

    world =[]

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    ball_big = [BallBig() for i in range(11)]
    ball_small = [BallSmall() for i in range(11)]
    world += ball_big + ball_small
    running = True

def update_world():
    for obj in world:
        obj.update()
def render_world():
    clear_canvas()

    for obj in world:
        obj.draw()

    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while(running):
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)


# finalization code

close_canvas()
