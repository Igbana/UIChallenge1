from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class Screen1(MDScreen):
    Builder.load_file('screen1.kv')

class MainApp(MDApp):
    def build(self):
        return Screen1()

MainApp().run()