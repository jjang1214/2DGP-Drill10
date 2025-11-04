from pico2d import *
import random

import game_world
import game_framework
from state_machine import StateMachine


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

frame = [
    (34,362,146,144),
    (216,364,146,142),
    (398,364,146,142),
    (554,360,172,140),
    (728,370,182,136),
    (34,170,146,120),
    (216,166,146,124),
    (398,170,146,120),
    (580,180,146,110),
    (762,178,146,110),
    (34,6,146,110),
    (216,4,146,106),
    (376,22,168,90),
    (546,22,180,116)
]

class Fly:
    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        self.bird.frame = (self.bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.bird.x += self.bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.bird.x >= 1600 or self.bird.x <= 0:
            self.bird.dir *= -1
            self.bird.face_dir *= -1

    def draw(self):
        frame_index = int(self.bird.frame)
        x, y, w, h = frame[frame_index]

        if self.bird.face_dir == 1:
            self.bird.image.clip_draw(x, y, w, h, self.bird.x, self.bird.y)
        else:
            self.bird.image.clip_composite_draw(x, y, w, h, 0,'h',self.bird.x, self.bird.y,w,h)


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100,1500), 500
        self.frame = random.randint(0,13)
        self.dir = self.face_dir = random.choice([-1, 1])
        self.image = load_image('bird_animation.png')

        self.FLY = Fly(self)
        self.state_machine = StateMachine(
            self.FLY,
            {

            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()