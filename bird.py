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

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


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

    def draw(self):
        if self.bird.face_dir == 1:
            if 0 <= self.bird.frame <= 4:
                self.bird.image.clip_draw(int(self.bird.frame) * 181, 168*2, 170, 160, self.bird.x, self.bird.y)
            elif 5 <= self.bird.frame <= 9:
                self.bird.image.clip_draw(int(self.bird.frame-5) * 181, 168*1, 170, 160, self.bird.x, self.bird.y)
            elif 10 <= self.bird.frame <= 13:
                self.bird.image.clip_draw(int(self.bird.frame-10) * 181, 168*0, 170, 160, self.bird.x, self.bird.y)
        else:
            if 0 <= self.bird.frame <= 4:
                self.bird.image.clip_composite_draw(int(self.bird.frame) * 181, 168 * 2, 170, 160, self.bird.x, self.bird.y)
            elif 5 <= self.bird.frame <= 9:
                self.bird.image.clip_composite_draw(int(self.bird.frame - 5) * 181, 168 * 1, 170, 160, self.bird.x, self.bird.y)
            elif 10 <= self.bird.frame <= 13:
                self.bird.image.clip_composite_draw(int(self.bird.frame - 10) * 181, 168 * 0, 170, 160, self.bird.x, self.bird.y)



class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100,1500), 500
        self.frame = 0
        self.face_dir = 1
        self.dir = 1
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