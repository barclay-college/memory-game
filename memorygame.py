#!/usr/bin/python3

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty,\
ListProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from random import shuffle
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton

class WelcomeWindow(Screen):
    pass


class VerseTile(FloatLayout):


    verse_num = ObjectProperty(None)
    verse_text = ObjectProperty(None)
    revealed = BooleanProperty(False)
    matched = BooleanProperty(False)

    def reveal(self):
        self.ids.verse_button.opacity = 0
        self.ids.verse_label.opacity = 1
        self.ids.verse_label.revealed = True

class Game_Window(GridLayout):

    verses = []
    versetiles = []
    reveal_list = ListProperty([])

    def get_verses(self):
        gluke = "/home/carl/documents/church/bible_translation_work/gospel_of_luke.txt"
        with open(gluke) as file:
            verses = file.readlines()

        shuffle(verses)
        verses = verses[:4]
        verses.extend(verses)
        shuffle(verses)

        for verse in verses:
            self.verses.append(verse)

    def start_game(self):
       
        self.clear_widgets()
        self.get_verses()

        num_verses = len(self.verses)

        for i in range(num_verses):
            verse_number = "Verse {}".format(str(i+1))
            self.add_widget(VerseTile(
                verse_num=verse_number,
                verse_text=self.verses[i]))

    def reveal_verses(self):
        for versetile in self.children:
            for child in versetile.children:
                if isinstance(child, MDLabel):
                    if child.opacity == 1:
                        self.reveal_list.append(child)

    def check_matches(self):
        if len(self.reveal_list) <= 1:
            return
        else:
            for label in self.reveal_list:
                label.opacity = 0



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"


        return Builder.load_file("main.kv")


if __name__ == '__main__':
    MyApp().run()
