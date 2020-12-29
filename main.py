from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

# First, we have to import functionalities such as the "ScreenManager" in order for our Python code to run properly
# In the following part, some widgets are included which normally would also require importing, however,
# since it is written directly in Kivy code, this is not necessary.

Builder.load_string("""
<WelcomeScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 0.4, 0.4, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            id: welcomeLabel
            size_hint: 0.35, 0.2
            pos_hint: {"center_x":.5, "center_y":.50}
            text: "Welcome to Monolith"
            font_size: 80
            family_name: "arial"
            bold: True
        Button:
            id: enterButton
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":.5, "center_y":.35}
            text: "Go to Log in"
            font_size: 30
            family_name: "arial"
            background_color: 0, 0, 0, 1
            on_press:
                root.manager.transition.direction = "up"
                root.manager.transition.duration = 1
                root.manager.current = "login_sc"                

<LoginScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 0.4, 0.4, 1
            Rectangle:
                pos: self.pos
                size: self.size
        TextInput:
            id: usernameInput
            size_hint: 0.45, 0.08
            pos_hint: {"center_x":0.35, "center_y":0.57}
            hint_text: "Username or email"
            font_size: 28
            family_name: "arial"
            multiline: False
        TextInput:
            id: passwordInput
            size_hint: 0.45, 0.08
            pos_hint: {"center_x":0.35, "center_y":0.43}
            hint_text: "Password"
            font_size: 28
            family_name: "arial"
            multiline: False
            password: True
        Button:
            id: loginButton
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.75, "center_y":0.5}
            text: "Log in"
            font_size: 30
            family_name: "arial"
            background_color: 0, 0, 0, 1
            on_press:
                root.manager.transition.direction = "up"
                root.manager.transition.duration = 1
                root.manager.current = "main_sc"
            
<MainScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 0.4, 0.4, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            id: logoLabel
            text: "Monolith"
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.5, "center_y":0.5}
            font_size: 80
            bold: True
        Button:
            id: mapsButton
            text: "Maps"
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.25, "center_y":0.75}
            font_size: 30
            background_color: 0, 0, 0, 1
        Button:
            id: socialButton
            text: "Social Section"
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.75, "center_y":0.25}
            font_size: 30
            background_color: 0, 0, 0, 1
        Button:
            id: blackButton
            text: "Blackboard"
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.75, "center_y":0.75}
            font_size: 30
            background_color: 0, 0, 0, 1
        Button:
            id: activitiesButton
            text: "Activities"
            size_hint: 0.25, 0.1
            pos_hint: {"center_x":0.25, "center_y":0.25}
            font_size: 30
            background_color: 0, 0, 0, 1
""")

# In the code above, the three screens for the screen manager are defined (WelcomeScreen, LoginScreen, MainScreen)
# Widgets are added to them such as buttons, labels and text inputs
# On the first and the second screen, the buttons function as the trigger for the screen transition
# On press, the screen manager receives information about which screen to display next, what direction to slide the
# screens in and the duration of the transition


class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass

# The screens also have to be defined as classes in order to add them to the screen manager
# All functionalities of the classes are defined in the Kivy code above


screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name="welcome_sc"))
screen_manager.add_widget(LoginScreen(name="login_sc"))
screen_manager.add_widget(MainScreen(name="main_sc"))

# Here, the screens are simply added to the screen manager and given an id to recall them


class MonolithApp(App):

    def build(self):
        return screen_manager

# Finally, the App is built and told to display the first screen added to the manager


Window.fullscreen = True

MonolithApp().run()

# These are only the core concepts of our final project
# Not only the functions will be expanded but the GUI will also be revamped
