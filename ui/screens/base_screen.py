from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class BaseScreen(Screen):
    @property
    def session(self):
        return App.get_running_app().session
    