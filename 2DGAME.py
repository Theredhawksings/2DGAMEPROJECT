from mimetypes import read_mime_types

from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x,self.y = random.randint(0,700),90
        self.frame = 0
        self.image = load_image('run_animation1.png')

    def update(self):
        self.frame = (self.frame+1)%3

    def draw(self):
        self.image.clip_draw(self.frame*64, 64, 64, 64, self.x, self.y, 128,128)

def reset_world():
    global boy
    boy = Boy()

def update_world():
    boy.update()

def render_world():
    clear_canvas()
    boy.draw()
    update_canvas()


open_canvas()

reset_world()

while True:
    update_world()
    render_world()
    delay(0.05)

close_canvas()