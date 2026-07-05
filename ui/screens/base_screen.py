from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.screenmanager import ScreenManager, Screen
#from data.ApplicationContext import ApplicationContext
from data.config.constants import Constants
from ui.screens.navigator import navigatorMenu

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root_layout = BoxLayout(orientation="vertical")
        #self.title = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
        self.title = AnchorLayout()
        self.title.anchor_x = "center"
        self.title.anchor_y = "center"
        self.title.size_hint_y=None
        self.title.height=Constants.HEADER_HEIGHT
        self.status = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        self.content = BoxLayout()
        self.navigation = navigatorMenu(self.change_screen)
        self.root_layout.add_widget(self.title)
        self.root_layout.add_widget(self.status)
        self.root_layout.add_widget(self.content)
        self.root_layout.add_widget(self.navigation)
        self.add_widget(self.root_layout)
    
    @property
    def context(self):
        return App.get_running_app().context
    

    @property
    def session(self):
        return self.context.session
    
    
        
        
    