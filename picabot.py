#!/usr/bin/python2
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder

kv="""
<ContainerBox>
    BoxLayout:
        orientation:'vertical'
        padding:0,0,0,10
        spacing:15
        size_hint:1,1
        Image:
            source:'pics/titlebar.png'
            allow_stretch:True
            size_hint:1,0.45
        BoxLayout:
            orientation:'horizontal'
            padding:0,0,10,10
            BoxLayout:
                orientation:'vertical'
                spacing:5
                padding:20,0,0,0
                Button:
                    on_press:root.bProxieOnClick()
                    background_down:'pics/small_button_pressed.png'
                    background_normal:'pics/small_button_unpressed.png'
                    text:'[color=000000]Proxies[/color]'
                    markup:True
                    size_hint:.9,.5
                Button:
                    on_press:root.bAccontsOnClick()
                    background_down:'pics/small_button_pressed.png'
                    background_normal:'pics/small_button_unpressed.png'
                    text:'[color=000000]Accouts[/color]'
                    markup:True
                    size_hint:.9,.5
                Button:
                    on_press:root.bIdOnClick()
                    background_down:'pics/small_button_pressed.png'
                    background_normal:'pics/small_button_unpressed.png'
                    text:'[color=000000]Quote ID[/color]'
                    markup:True
                    size_hint:.9,.5
            BoxLayout:
                orientation:'vertical'
                Label:
                    text:'[color=69d369]Filled[/color]'
                    markup:True
                Label:
                    text:'[color=69d369]Filled[/color]'
                    markup:True
                Label:
                    text:'[color=69d369]Filled[/color]'
                    markup:True
            Image:
                source:'pics/help.png'
                size_hint:1.5,1.5
                pos_hint:{'top':1,'bottom':.9}
            Button:
                on_press:root.bHelpOnClick()
                background_down:'pics/small_button_pressed.png'
                background_normal:'pics/small_button_unpressed.png'
                text:'[color=000000][b][size=30]?[/size][/b][/color]'
                markup:True
                size_hint:.25,.55
                pos_hint:{'top':1,'right':0}
        BoxLayout:
            orientation:'horizontal'
            spacing:20
            padding:20,0,20,0
            Button:
                on_press:root.bLoveOnClick()
                background_down:'pics/small_button_pressed.png'
                background_normal:'pics/small_button_unpressed.png'
                text:'[color=000000]Absolutly Love[/color]'
                markup:True
                size_hint:.1,.55
            Button:
                on_press:root.bHateOnClick()
                background_down:'pics/red_btn_pressed.png'
                background_normal:'pics/red_btn.png'
                text:'[color=000000]Totally Hate[/color]'
                markup:True
                size_hint:.1,.55
        Button:
            on_press:root.bCookieOnClick()
            background_down:'pics/cookie_pressed.png'
            background_normal:'pics/cookie.png'
            pos_hint:{'center_x':.5,'center_y':.5}
            size_hint:.15,1
        Label:
            text:'[color=69d369]Fill the fields[/color]'
            markup:True
            pos_hint:{'center_x':.5}
            size_hint:.1,.1
        ProgressBar:
            max:100
            pos_hint:{'center_x':.5}
            size_hint:.7,.3
"""
Builder.load_string(kv)

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        Config.set('input','mouse','mouse,multitouch_on_demand')
        Config.set('graphics','resizable',0)
        Config.set('graphics','width',800)
        Config.set('graphics','height',600)
        super(ContainerBox, self).__init__(**kwargs)

    def bProxieOnClick(self):
        print("Proxie")
    def bAccontsOnClick(self):
        print("Accounts")
    def bIdOnClick(self):
        print("ID")
    def bHelpOnClick(self):
        print("help")
    def bLoveOnClick(self):
        print("love")
    def bHateOnClick(self):
        print("hate")
    def bCookieOnClick(self):
        print("cookie")

class PicabotApp(App):
    
    def build(self):
        return ContainerBox()

if __name__ == "__main__":
    PicabotApp().run()

