#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import logging

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock


class Square(Widget):
    growth = 0.17
    velocity = ListProperty([10, 15])
    moved = False

    def __init__(self, **kwargs):
        super(Square, self).__init__(**kwargs)

    def grow(self):
        self.width += self.growth / 2
        self.parent.x -= self.growth / 4
        self.height += self.growth / 2
        self.parent.y -= self.growth / 4

        # if (self.x + self.width) > Window.width:
        # self.x -= self.growth
        # if (self.y + self.height) > Window.height:
        # self.y -= self.growth
        # if self.x - self.width <0:
        # self.x += self.growth
        # if self.y - self.height <0:
        # self.y += self.growth

    def on_touch_move(self, touch):
        self.moved = True


    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):  # this checks if we clicked on a child or on the parent
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

    @staticmethod
    def stop_all_children(parent):
        for child in parent.children:
            child.children[0].growth = 0

    def update(self, dt):
        for child in self.children:
            child.children[0].grow()

            if child.y < 0:
                child.y += child.children[0].growth
            if child.top > self.height:
                child.y -= child.children[0].growth
            if child.x < 0:
                child.x += child.children[0].growth
            if child.right > self.width:
                child.x -= child.children[0].growth

            for other_child in self.children:
                if child != other_child:
                    if child.collide_widget(other_child):
                        self.stop_all_children(self)


class GrowthApp(App):
    def build(self):
        game = MainScreenScatter()
        Clock.schedule_interval(game.update, 1 / 60)
        return game


if __name__ == '__main__':
    GrowthApp().run()
