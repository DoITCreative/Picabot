#!/usr/bin/python2
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar



class PicabotApp(App):
    
    def build(self):


        Config.set('input','mouse','mouse,multitouch_on_demand')
        Config.set('graphics','resizable',0)
        Config.set('graphics','width',800)
        Config.set('graphics','height',600)

        boxl=BoxLayout(
                orientation="vertical",
                padding=(0,0,0,10),
                spacing=15,
                size_hint=(1,1)
                )
        picaimg=Image(
                source='pics/titlebar.png',
                allow_stretch='true',
                size_hint=(1,0.45)
                )
        boxl1=BoxLayout(
                orientation='horizontal',
                padding=(0,0,10,10)
                )
        boxl2=BoxLayout(
                orientation='vertical',
                spacing=5,
                padding=(20,0,0,0)
                )
        
        bProxie = Button(
            background_down='pics/small_button_pressed.png',
            background_normal='pics/small_button_unpressed.png',
            text='[color=000000]Proxies[/color]',
            markup='true',
            size_hint=(0.9,.5)
            )

        bAccounts = Button(
            background_down='pics/small_button_pressed.png',
            background_normal='pics/small_button_unpressed.png',
            text='[color=000000]Accouts[/color]',
            markup='true',
            size_hint=(0.9,.5)
            )

        bId = Button(
            background_down='pics/small_button_pressed.png',
            background_normal='pics/small_button_unpressed.png',
            text='[color=000000]Quote ID[/color]',
            markup='true',
            size_hint=(0.9,.5)
            )
       
        boxl3=BoxLayout(orientation='vertical')
        lProxies = Label (
                    text='[color=69d369]Filled[/color]',
                    markup='true'
                )
        lAccounts = Label (
                    text='[color=69d369]Filled[/color]',
                    markup='true'
                )
        lQuoteID = Label (
                    text='[color=69d369]Filled[/color]',
                    markup='true'
                )

        helpImg=Image(
                source='pics/help.png',
                size_hint=(1.5,1.5),
                pos_hint={
                    'top':1,
                    'bottom':0.9
                    })
        bHelp = Button(
            background_down='pics/small_button_pressed.png',
            background_normal='pics/small_button_unpressed.png',
            text='[color=000000][b][size=30]?[/size][/b][/color]',
            markup='true',
            size_hint=(.25,.55),
            pos_hint={
                'top':1,
                'right':0            
                }
            )
       
        boxl4=BoxLayout(
                orientation='horizontal',
                spacing=20,
                padding=(20,0,20,0)
                )
        bLove = Button(
            background_down='pics/small_button_pressed.png',
            background_normal='pics/small_button_unpressed.png',
            text='[color=000000]Absolutly Love[/color]',
            markup='true',
            size_hint=(.1,.55)
            )
       
        bHate = Button(
            background_down='pics/red_btn_pressed.png',
            background_normal='pics/red_btn.png',
            text='[color=000000]Totally Hate[/color]',
            markup='true',
            size_hint=(.1,.55)
            )
       
        bCookie = Button(
            background_down='pics/cookie_pressed.png',
            background_normal='pics/cookie.png',
            text='',
            pos_hint={
                'center_x':0.5,
                'center_y':0.5
                },
            size_hint=(0.15,1)
            )
       
        lProgress = Label (
                    text='[color=69d369]Fill the fields[/color]',
                    markup='true',
                    pos_hint={
                        'center_x':0.5
                        },
                    size_hint=(0.1,0.1)
                    )
        pBar = ProgressBar(
                max=100,
                background_color=(0,255,0,255),
                pos_hint={
                    'center_x':0.5
                    },
                size_hint=(0.7,0.3)
                )

        pBar.value=75

#boxl vert
#   picabotlogo
#   boxl1 horiz
#       boxl2 vert
#           bProxie
#           bAccounts
#           bId
#       boxl3 vert
#           done1
#           done2
#           done3
#       help
#       question
#   boxl4 horiz
#       love
#       hate
#   cookie
#   label
#   pBar

        boxl.add_widget(picaimg)
        boxl.add_widget(boxl1)
        boxl1.add_widget(boxl2)
        boxl2.add_widget(bProxie)
        boxl2.add_widget(bAccounts)
        boxl2.add_widget(bId)
        boxl1.add_widget(boxl3)
        boxl3.add_widget(lProxies)
        boxl3.add_widget(lAccounts)
        boxl3.add_widget(lQuoteID)
        boxl1.add_widget(helpImg)
        boxl1.add_widget(bHelp)
        boxl.add_widget(boxl4)
        boxl4.add_widget(bLove)
        boxl4.add_widget(bHate)
        boxl.add_widget(bCookie)
        boxl.add_widget(lProgress)
        boxl.add_widget(pBar)

# Button bindings bellow
        bProxie.bind(on_press=self.bProxieOnClick)
        bAccounts.bind(on_press=self.bAccontsOnClick)
        bId.bind(on_press=self.bIdOnClick)
        bHelp.bind(on_press=self.bHelpOnClick)
        bLove.bind(on_press=self.bLoveOnClick)
        bHate.bind(on_press=self.bHateOnClick)
        bCookie.bind(on_press=self.bCookieOnClick)


        return boxl

    def bProxieOnClick(self,obj):
        print("Proxie")
    def bAccontsOnClick(self,obj):
        print("Accounts")
    def bIdOnClick(self,obj):
        print("ID")

    def bHelpOnClick(self,obj):
        print("help")
    def bLoveOnClick(self,obj):
        print("love")
    def bHateOnClick(self,obj):
        print("hate")
    def bCookieOnClick(self,obj):
        print("cookie")

if __name__ == "__main__":
    PicabotApp().run()

