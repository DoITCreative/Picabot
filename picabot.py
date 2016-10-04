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



class PicabotApp(App):
    def build(self):
        Config.set('input','mouse','mouse,multitouch_on_demand')
        Config.set('graphics','resizable',0)
        Config.set('graphics','width',800)
        Config.set('graphics','height',600)

        boxl=BoxLayout(
                orientation="vertical",
                padding=(0,0,0,10),
                size_hint=(1,1)
                )
        picaimg=Image(
                source='pics/titlebar.png',
                allow_stretch='true',
                size_hint=(1,1),
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
            size_hint=(.13,1),
            pos_hint={'center_x':0.5}
            )
       

        floatl = FloatLayout(padding=(10,0,0,10))
        bbfImg=Image(
                source='pics/bottom_bar_filled.png',
                size_hint=(1,0.2),
                pos_hint={'center_x':0.5}
                )
        bbufImg=Image(
                source='pics/bottom_bar_unfilled.png',
                size_hint=(1,0.2),
                pos_hint={'center_x':0.5}
                )

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
#   floatl
#       line
#       linegreen


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
        boxl.add_widget(floatl)
        floatl.add_widget(bbufImg)
        floatl.add_widget(bbfImg)



        return boxl


if __name__ == "__main__":
    PicabotApp().run()

