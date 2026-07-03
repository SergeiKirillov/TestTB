from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.setting import Setting
from ui.screens.theme import Theme
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp, sp
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen

class MainScreen(BaseScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        blMain = BoxLayout(orientation="vertical")

        lblTitle=Label(text="Главный экрaн", color="yellow")
        lblTitle.font_size=Constants.HEADER_HEIGHT*0.5

        #btnTheme=Button(text="Выбор темы заданий",size_hint=(None, None),size=(200,20))
        #btnTheme.id="btn_select_theme"
        #btnTheme.bind(on_release=self.btn_click)

        blMain.add_widget(lblTitle)
        #blMain.add_widget(btnTheme)
        blMain.add_widget(navigatorMenu(self.change_screen))

        self.session.user="019261"

        self.add_widget(blMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen


#    def btn_click(self, instance):  
#        #print(self.manager.current)
#        self.manager.current = "theme"





    

    

