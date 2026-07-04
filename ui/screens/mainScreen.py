from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
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
        blMain = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(10))
        blMainTitle = BoxLayout(orientation="horizontal", padding=dp(10), spacing=dp(10))
        blMainContent = BoxLayout(orientation="horizontal", padding=dp(10), spacing=dp(10))
        blMainMenu = BoxLayout(orientation="horizontal", padding=dp(10), spacing=dp(10))
        blMainLeft = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(10), size_hint=(None, 1), width=dp(200))
        blMainRight = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(10),size_hint=(None, 1), width=dp(200))
        blMainCenter = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(10))

        blMainTitle.add_widget(Label(text="Главный экран", color="yellow", font_size=Constants.HEADER_HEIGHT*0.5))
        txtLoginName=TextInput(_hint_text="Введите табельный номер, и нажмите Enter", size_hint=(None, None), size=(500, 30),multiline=False)
        txtLoginName.input_filter = "int"  # Ограничение ввода только цифрами
        txtLoginName.bind(on_text_validate=self.on_enter_pressed)
        txtLoginName.bind(text=self.limit_length)  # Ограничение длины ввода
        #

       
        #btnLoginName=Button(text="Войти",size_hint=(None, None),size=(200,25))    
        blMainCenter.add_widget(Widget())  # Добавляем пустой виджет для отступа
        blMainCenter.add_widget(txtLoginName)
        #blMainCenter.add_widget(btnLoginName)
        blMainCenter.add_widget(Widget())  # Добавляем пустой виджет для отступа
        blMainContent.add_widget(blMainLeft)
        blMainContent.add_widget(blMainCenter)
        blMainContent.add_widget(blMainRight)
        blMainMenu.add_widget(navigatorMenu(self.change_screen))
        blMain.add_widget(blMainTitle)
        blMain.add_widget(blMainContent)
        blMain.add_widget(blMainMenu)


        #btnTheme=Button(text="Выбор темы заданий",size_hint=(None, None),size=(200,20))
        #btnTheme.id="btn_select_theme"
        #btnTheme.bind(on_release=self.btn_click)

        #blMainTitle.add_widget(lblTitle)
        #blMain.add_widget(blMainTitle)
        #blMain.add_widget(btnTheme)
        #blMain.add_widget(navigatorMenu(self.change_screen))

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

#TODO: добавить обработку нажатия Enter в TextInput
    def on_enter_pressed(self, instance):
        self.session.user=instance.text
        self.change_screen("theme")  # Переход на экран выбора темы

#TODO:ограничение кол-ва вводимых знаков
    def limit_length(self, instance, value):
        max_length = 8  # Максимальная длина ввода
        if len(value) > max_length:
            instance.text = value[:max_length]





    

    

