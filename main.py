from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"

    BoxLayout:
        orientation: "vertical"
        padding: 40
        spacing: 20

        Label:
            text: "Login"
            font_size: 32

        TextInput:
            id: username
            hint_text: "Username"
            multiline: False

        TextInput:
            id: password
            hint_text: "Password"
            password: True
            multiline: False

        Button:
            text: "Login"
            on_press: root.login()

        Label:
            id: message
            text: ""

<HomeScreen>:
    name: "home"

    BoxLayout:
        orientation: "vertical"

        Label:
            text: "Welcome!"
            font_size: 30

        Button:
            text: "Logout"
            on_press: app.root.current = "login"
'''

class LoginScreen(Screen):
    def login(self):
        user = self.ids.username.text
        pwd = self.ids.password.text

        if user == "admin" and pwd == "1234":
            self.manager.current = "home"
        else:
            self.ids.message.text = "Invalid login"

class HomeScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    MyApp().run()
