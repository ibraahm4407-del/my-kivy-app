 import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


# LOGIN SCREEN
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.user = TextInput(hint_text="Username")
        self.passw = TextInput(hint_text="Password", password=True)

        login_btn = Button(text="Login")
        login_btn.bind(on_press=self.login)

        reg_btn = Button(text="Go to Register")
        reg_btn.bind(on_press=lambda x: setattr(self.manager, 'current', "register"))

        self.msg = Label(text="")

        layout.add_widget(self.user)
        layout.add_widget(self.passw)
        layout.add_widget(login_btn)
        layout.add_widget(reg_btn)
        layout.add_widget(self.msg)

        self.add_widget(layout)

    def login(self, instance):
        url = "https://flask-app-1-lbn4.onrender.com/login"

        data = {
            "username": self.user.text,
            "password": self.passw.text
        }

        try:
            res = requests.post(url, json=data)

            if res.status_code == 200:
                user_data = res.json()
                username = user_data.get("username")

                self.manager.get_screen("home").user_label.text = "Welcome " + username
                self.manager.current = "home"
            else:
                self.msg.text = "Login failed"

        except:
            self.msg.text = "Server error"


# REGISTER SCREEN
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.user = TextInput(hint_text="Username")
        self.passw = TextInput(hint_text="Password", password=True)

        reg_btn = Button(text="Register")
        reg_btn.bind(on_press=self.register)

        back_btn = Button(text="Back to Login")
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', "login"))

        self.msg = Label(text="")

        layout.add_widget(self.user)
        layout.add_widget(self.passw)
        layout.add_widget(reg_btn)
        layout.add_widget(back_btn)
        layout.add_widget(self.msg)

        self.add_widget(layout)

    def register(self, instance):
        url = "https://flask-app-1-lbn4.onrender.com/register"

        data = {
            "username": self.user.text,
            "password": self.passw.text
        }

        try:
            res = requests.post(url, json=data)

            if res.status_code == 200:
                self.msg.text = "Registered!"
            else:
                self.msg.text = "Error"

        except:
            self.msg.text = "Server not reachable"


# HOME SCREEN
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.user_label = Label(text="Welcome!")
        layout.add_widget(self.user_label)

        logout_btn = Button(text="Logout")
        logout_btn.bind(on_press=lambda x: setattr(self.manager, 'current', "login"))

        layout.add_widget(logout_btn)

        self.add_widget(layout)


# MAIN APP
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(HomeScreen(name="home"))
        return sm


MyApp().run()
