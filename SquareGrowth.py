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
import random


class Square(Widget):

    pass


class Squatter(Widget):

    pass


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
