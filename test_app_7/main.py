#!/usr/bin/env python2

import os
import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class TopBox(BoxLayout):
    
    def button_click(self):
        
        text_split = self.ids['label1'].text.split(' ')

        new_text = "%d clicks" % (int(text_split[0]) + 1)

        self.ids['label1'].text = new_text


class TestApp(App):

    def build(self):

        return TopBox()

if __name__ == "__main__":

    kivy.require('1.10.1')

    kivy_file = resource_path('style.kv')

    Builder.load_file(kivy_file)

    TestApp().run()
