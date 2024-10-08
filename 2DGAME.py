from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,700), 90
        self.frame = 0
        self.image = load_image('run_animation1.png')
        self.dx, self.dy = 0, 0
        self.stop = True
        self.right = True

    def update(self):
        if self.dx != 0 or self.dy != 0:
            self.frame = (self.frame + 1) % 3

        self.x += self.dx
        self.y += self.dy

    def draw(self):
        if self.right:
            self.image.clip_draw(self.frame * 64, 64, 64, 64, self.x, self.y, 128, 128)
        else:
            self.image.clip_draw(self.frame * 64, 128, 64, 64, self.x, self.y, 128, 128)

    def move(self, dx, dy):
        self.dx, self.dy = dx, dy

def reset_world():
    global boy, running, key_states
    boy = Boy()
    running = True
    key_states = {'w': False, 'a': False, 's': False, 'd': False}

def update_boy_movement():
    boy.dx, boy.dy = 0, 0
    if key_states['d']:
        boy.dx += 5
        boy.right = True
    if key_states['a']:
        boy.dx -= 5
        boy.right = False
    if key_states['w']: boy.dy += 5
    if key_states['s']: boy.dy -= 5

def update_world():
    update_boy_movement()
    boy.update()

def render_world():
    clear_canvas()
    boy.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_w:
                key_states['w'] = True
            elif event.key == SDLK_s:
                key_states['s'] = True
            elif event.key == SDLK_a:
                key_states['a'] = True
            elif event.key == SDLK_d:
                key_states['d'] = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                key_states['w'] = False
            elif event.key == SDLK_s:
                key_states['s'] = False
            elif event.key == SDLK_a:
                key_states['a'] = False
            elif event.key == SDLK_d:
                key_states['d'] = False

open_canvas(800, 600)

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()