from pico2d import *
import random

class Ground:
    def __init__(self):
        self.image = load_image('Ground1.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 50, 100
        self.frame = 0
        self.image = load_image('run_animation1.png')
        self.dx, self.dy = 0, 0
        self.stop = True
        self.right = True
        self.is_jumping = False
        self.jump_speed = 0
        self.gravity = -1
        self.ground_y = 100

    def update(self):
        if self.dx != 0 or self.dy != 0:
            self.frame = (self.frame + 1) % 3

        self.x += self.dx

        if self.is_jumping:
            self.y += self.jump_speed
            self.jump_speed += self.gravity

            if self.y <= self.ground_y:
                self.y = self.ground_y
                self.is_jumping = False
                self.jump_speed = 0
        else:
            self.y += self.dy

    def draw(self):
        if self.right:
            self.image.clip_draw(self.frame * 64, 64, 64, 64, self.x, self.y, 128, 128)
        else:
            self.image.clip_draw(self.frame * 64, 128, 64, 64, self.x, self.y, 128, 128)

    def move(self, dx, dy):
        self.dx, self.dy = dx, dy

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = 13


def reset_world():
    global boy, grass, ground, running, key_states
    boy = Boy()
    grass = Grass()
    ground = Ground()
    running = True
    key_states = {'w': False, 'a': False, 's': False, 'd': False, 'space': False}


def update_boy_movement():
    boy.dx, boy.dy = 0, 0
    if key_states['d']:
        boy.dx += 7
        boy.right = True
    if key_states['a']:
        boy.dx -= 7
        boy.right = False
    if key_states['w'] and not boy.is_jumping: boy.dy += 7
    if key_states['s'] and not boy.is_jumping: boy.dy -= 7
    if key_states['space']:
        boy.jump()


def update_world():
    update_boy_movement()
    boy.update()
    grass.update()
    ground.update()


def render_world():
    clear_canvas()
    ground.draw()
    grass.draw()
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
            elif event.key == SDLK_a:
                key_states['a'] = True
            elif event.key == SDLK_d:
                key_states['d'] = True
            elif event.key == SDLK_SPACE:
                key_states['space'] = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                key_states['a'] = False
            elif event.key == SDLK_d:
                key_states['d'] = False
            elif event.key == SDLK_SPACE:
                key_states['space'] = False


open_canvas(800, 600)

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()