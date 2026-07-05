from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
#from data.ApplicationContext import ApplicationContext

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @property
    def context(self):
        return App.get_running_app().context

    @property
    def session(self):
        return self.context.session
        
        
    