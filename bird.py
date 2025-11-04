from pico2d import *

import game_world
import game_framework
from state_machine import StateMachine


class Fly:
    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        pass



class Bird:
    def __init__(self):
        self.x, self.y = 400, 500
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')

        self.FLY = Fly(self)
        self.state_machine = StateMachine(
            self.FLY,
            {

            }
        )

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        pass