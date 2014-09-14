#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock
from functools import partial
import random


class ScatterTextWidget(BoxLayout):

    text_color = ObjectProperty([1, 0, 0, 1])
    scatter_size_x = ObjectProperty(1)
    scatter_size_y = ObjectProperty(1)
    scatter_pos = ObjectProperty([150, 150])
    growth_rate = 0.25
    pressed = False

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

        def grow(*args):
            self.scatter_size_x += self.growth_rate
            self.scatter_size_y += self.growth_rate

        Clock.schedule_interval(grow, 0.017)

    def toggle_growth(self, *args):
        if self.pressed:
            if self.growth_rate == 0:
                self.growth_rate = 0.25
            else:
                self.growth_rate = 0
            self.pressed = False
        else:
            self.pressed = True

    def change_label_color(self, *args):
        c = [random.random() for i in range(4)]
        self.text_color = c


class TutorialApp(App):

    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    TutorialApp().run()
