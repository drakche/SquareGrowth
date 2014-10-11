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
import logging


class Square(Widget):
    growth = 0.17
    velocity = ListProperty([10, 15])
    moved = False

    def __init__(self, **kwargs):
        super(Square, self).__init__(**kwargs)

    def grow(self):
        self.width += self.growth

        self.height += self.growth

        # if (self.x + self.width) > Window.width:
        # self.x -= self.growth
        # if (self.y + self.height) > Window.height:
        # self.y -= self.growth
        # if self.x - self.width <0:
        #     self.x += self.growth
        # if self.y - self.height <0:
        #     self.y += self.growth

    def on_touch_move(self, touch):
        self.moved = True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos): #this checks if we clicked on a child or on the parent
            if not self.moved:
                if self.growth != 0:
                    self.growth = 0
                else:
                    self.growth = 0.17
            else:
                self.moved = False
            return True
        else:
            return False


class MainScreenScatter(FloatLayout):
    scatter = ObjectProperty(None)
    # square = ObjectProperty(None)

    @staticmethod
    def getrandomposition():
        return [random.random() * Window.width, random.random()
                * Window.height]

    def update(self, dt):
        for child in self.children:
            child.children[0].grow()
            # logging.info(str(self.scatter.right))
            # logging.info(str(self.width))
            if child.y + child.height < 0:
                child.y += child.children[0].growth
            if child.top + child.height > child.height:
                child.y -= child.children[0].growth
            if child.x + child.width < 0:
                child.x += child.children[0].growth
            if child.right > child.width:
                logging.info('end hit')
                child.x -= child.children[0].growth


class GrowthApp(App):
    def build(self):
        game = MainScreenScatter()
        Clock.schedule_interval(game.update, 1 / 60)
        return game


if __name__ == '__main__':
    GrowthApp().run()
