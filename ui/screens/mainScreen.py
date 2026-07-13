from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
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

        self.title.add_widget(
            Label(text="Программа для проверки знаний", color="yellow", font_size=Constants.HEADER_HEIGHT*0.5)
        )
        blCenter=BoxLayout()
        blCenter.orientation="vertical"
        
        txtLoginName=TextInput(_hint_text="Введите табельный номер, и нажмите Enter", size_hint=(None, None), size=(500, 30),multiline=False)
        txtLoginName.input_filter = "int"  # Ограничение ввода только цифрами
        txtLoginName.bind(on_text_validate=self.on_enter_pressed)
        txtLoginName.bind(text=self.limit_length)  # Ограничение длины ввода
        
        self.lblLoginNameStatus = Label()
        self.lblLoginNameStatus.text=""
        self.lblLoginNameStatus.color="red"
        self.lblLoginNameStatus.font_size=Constants.HEADER_HEIGHT*0.3
        

        self.status.add_widget(self.lblLoginNameStatus)

        
        contentCenterAnchor=AnchorLayout(anchor_x = "center",anchor_y = "center")
        
#        contentCenterAnchor.add_widget(txtLoginName)
#        
#        blCenter.add_widget(contentCenterAnchor)
#        blCenter.add_widget(self.lblLoginNameStatus)
#        self.contentCenter.add_widget(blCenter)


#        blCenter.add_widget(Widget())
#        blCenter.add_widget(txtLoginName)
#        blCenter.add_widget(self.lblLoginNameStatus)
#        blCenter.add_widget(Widget())
#        contentCenterAnchor.add_widget(blCenter)

        contentCenterAnchor.add_widget(txtLoginName)
        self.contentCenter.add_widget(contentCenterAnchor)



    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen


#    def btn_click(self, instance):  
#        #print(self.manager.current)
#        self.manager.current = "theme"

#TODO: Обработку нажатия Enter в TextInput поля ввода табельного номера
    def on_enter_pressed(self, instance):
        
        user = self.database.load_user(instance.text)
        print(type(user))
        if user is not None:
            self.session.user=instance.text
            #self.context.session.user=instance.text           
            self.change_screen("theme")  # Переход на экран выбора темы
        else:
            self.lblLoginNameStatus.text="Нет такого пользователя"


        

#TODO:ограничение кол-ва вводимых знаков в проле ввода табельного номера
    def limit_length(self, instance, value):
        max_length = 8  # Максимальная длина ввода
        if len(value) > max_length:
            instance.text = value[:max_length]





    

    

