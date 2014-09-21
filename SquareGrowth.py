#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.animation import Animation
import random


class Square(Widget):

    growth = 0.1
    velocity = ListProperty([10, 15])
    moved = False

    def __init__(self, **kwargs):
        super(Square, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 60.)

    def update(self, *args):
        self.width += self.growth

        self.height += self.growth


        # if (self.x + self.width) > Window.width:
        #     self.x -= self.growth
        # if (self.y + self.height) > Window.height:
        #     self.y -= self.growth
        # if self.x - self.width <0:
        #     self.x += self.growth
        # if self.y - self.height <0:
        #     self.y += self.growth


    def on_touch_move(self, touch):
        self.moved = True

    def on_touch_up(self, touch):
        if self.moved == False:
            if self.growth != 0:
                self.growth = 0
            else:
                self.growth = 0.1
        else:
            self.moved = False


class MainScreenScatter(FloatLayout):

    def getRandPos(*args):
        return [random.random() * Window.width, random.random()
                * Window.height]

    pass


class GrowthApp(App):

    def build(self):
        return MainScreenScatter()


if __name__ == '__main__':
    GrowthApp().run()
