from mimetypes import read_mime_types

from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x,self.y = random.randint(0,700),90
        self.frame = 0
        self.image = load_image('run_animation1.png')
        self.dx, self.dy = 0, 0

    def update(self):
        self.frame = (self.frame+1)%3
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        self.image.clip_draw(self.frame*64, 64, 64, 64, self.x, self.y, 128,128)

    def move(self,dx,dy):
        self.dx, self.dy = dx, dy

def reset_world():
    global boy
    global running
    boy = Boy()
    running = True

def update_world():
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            boy.move(0, 5)

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()