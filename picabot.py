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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import requests
import sys
import time
import random
kv="""
<Manager>:
    id:myManager
    MainMenu:
        manager:myManager
        id:main_menu
        name:"Picabot"
    SelectionMenu1:
        manager:myManager
        name:"Your proxy"
    SelectionMenu2:
        manager:myManager
        name:"Your account"
    SelectionMenu3:
        manager:myManager
        name:"Your id"
<MainMenu>:
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
                    opacity:0
                    id:lDone1
                    text:'[color=69d369]Filled[/color]'
                    markup:True
                Label:
                    opacity:0
                    id:lDone2
                    text:'[color=69d369]Filled[/color]'
                    markup:True
                Label:
                    opacity:0
                    id:lDone3
                    text:'[color=69d369]Filled[/color]'
                    markup:True
            Image:
                id:iHelp
                opacity:0
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
            id:lOut
            text:'[color=69d369]Fill the fields.[/color]'
            markup:True
            pos_hint:{'center_x':.5}
            size_hint:.1,.1
        ProgressBar:
            id:pBar
            max:100
            pos_hint:{'center_x':.5}
            size_hint:.7,.3
<SelectionMenu1>:
    FloatLayout:
        Label:
            text:"Select path to your Proxy file:"
            size_hint:.1,.1
            pos_hint:{'center_x':0.2,'center_y':.8}
        TextInput:
            id:tProxy
            multiline:False
            size_hint:.6,.05
            pos_hint:{'center_x':0.5,'center_y':.5}
        BoxLayout:
            orientation:'horizontal'
            Button:
                text:"Confirm"
                on_press:root.bConfirmOnClick()
                size_hint:.1,.1
            Button:
                text:"Cancel"
                on_press:root.manager.current="Picabot"
                size_hint:.1,.1
<SelectionMenu2>:
    FloatLayout:
        Label:
            text:"Select path to your file with Accounts:"
            size_hint:.1,.1
            pos_hint:{'center_x':0.2,'center_y':.8}
        TextInput:
            id:tAccounts
            multiline:False
            size_hint:.6,.05
            pos_hint:{'center_x':0.5,'center_y':.5}
        BoxLayout:
            orientation:'horizontal'
            Button:
                text:"Confirm"
                on_press:root.bConfirmOnClick()
                size_hint:.1,.1
            Button:
                text:"Cancel"
                on_press:root.manager.current="Picabot"
                size_hint:.1,.1
<SelectionMenu3>:
    FloatLayout:
        Label:
            text:"Select ID of the quote:"
            size_hint:.1,.1
            pos_hint:{'center_x':0.2,'center_y':.8}
        TextInput:
            id:tId
            multiline:False
            size_hint:.6,.05
            pos_hint:{'center_x':0.5,'center_y':.5}
        BoxLayout:
            orientation:'horizontal'
            Button:
                text:"Confirm"
                on_press:root.bConfirmOnClick()
                size_hint:.1,.1
            Button:
                text:"Cancel"
                on_press:root.manager.current="Picabot"
                size_hint:.1,.1
"""
Builder.load_string(kv)
postid=""
likeornot=""
loginfilepath=""
proxyfilepath=""
proxiesFilled=0
accountFilled=0
idFilled=0
choiceFilled=0
class MainMenu(Screen):
    def bProxieOnClick(self):
        self.manager.current="Your proxy"
    def bAccontsOnClick(self):
        self.manager.current="Your account"
    def bIdOnClick(self):
        self.manager.current="Your id"
    def bHelpOnClick(self):
        if (self.ids.iHelp.opacity==1):
            self.ids.iHelp.opacity=0
            self.ids.lOut.text="[color=69d369]Help is hidden now.[/color]"
        else:
            self.ids.iHelp.opacity=1
            self.ids.lOut.text="[color=69d369]Help is shown now.[/color]"
    def bLoveOnClick(self):
        global choiceFilled
        global likeornot
        choiceFilled=1
        likeornot="1"
        self.ids.lOut.text="[color=69d369]Selected option: Love.[/color]"
    def bHateOnClick(self):
        global choiceFilled
        global likeornot
        choiceFilled=1
        likeornot="-1"
        self.ids.lOut.text="[color=69d369]Selected option: Hate.[/color]"
    def bCookieOnClick(self):
        if (proxiesFilled+accountFilled+idFilled+choiceFilled==4):

            try:
                loginfile = open(loginfilepath,'r')
                proxyfile = open(proxyfilepath,'r')
            except:
                self.ids.lOut.text="[color=69d369]Check your data.[/color]"
            else:
                logins=[]
                passwords=[]
                proxys=[]
                proxystype=[]
                count=0
                loginsnum=0
                proxysnum=0
                for line in loginfile:
                    s = line
                    s1,s2 = s.split(':')
                    logins.append(s1)
                    passwords.append(s2[:-1])
                for line in proxyfile:
                    s = line
                    s1,s2 = s.split()
                    proxystype.append(s1)
                    proxys.append(s2[:-1])
                for line in logins:
                    loginsnum=loginsnum+1
                for line in proxys:
                    proxysnum=proxysnum+1
                if proxysnum>=loginsnum:
                    count=loginsnum
                else:
                    count=proxysnum
                self.ids.pBar.max=count
                self.ids.pBar.value=0
                for k in range(0,count):
#                    sendreq(logins[k],passwords[k],str(postid),proxystype[k],proxys[k],str(likeornot))
                    print(logins[k],passwords[k],str(postid),proxystype[k],proxys[k],str(likeornot))
                    self.ids.pBar.value=self.ids.pBar.value+1
                    time.sleep(random.random()+int(random.random()*2)+1)
                self.ids.lOut.text="[color=69d369]Done![/color]"
        else:
            self.ids.lOut.text="[color=69d369]You must fill all the fields before pressing it![/color]"
    def sendreq(login, password, storyid, proxytype, proxy, vote):
        mproxies = {
                proxytype : proxytype+"://"+proxy
                }
        mheaders = {
                'Host':'pikabu.ru',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Language':'en-US,en;q=0.5',
                'Accept-Encoding':'gzip, deflate',
                'X-CSRF-Token':'t5fhrka497b005npsh387ffaj0rk5f7i',
                'x-requested-with':'x-requested-with: XMLHttpRequest',
                'Content-Length':str(69+len(login))
                }
        mdata = {
                "username":login,
                "password":password,
                "g-recaptcha-response":"",
                "mode":"login"
                }
        m2data = {
                "story_id":storyid,
                "vote":vote
                }
        m1cookies = {
                'PHPSESS':'t5fhrka497b005npsh387ffaj0rk5f7i',
                'is_scrollmode':'1',
                'autohide_news':'0',
                '_nuser':'1',
                'nps7s':'2148041329',
                'vn_buff':'[%22190f158bef%22%2C[]]',
                'la':'1',
                'set_autohide_news':'-1'
                }
        if proxy!="none":
            r = requests.post("http://pikabu.ru/ajax/auth.php", proxies=mproxies, data=mdata,headers=mheaders,cookies=m1cookies)
        else:
            r = requests.post("http://pikabu.ru/ajax/auth.php", data=mdata,headers=mheaders,cookies=m1cookies)
        m2cookies = m1cookies
        m2cookies['phpDug2']=r.cookies.get_dict()['phpDug2']
        if proxy!="none":
            r1 = requests.post("http://pikabu.ru/ajax/vote_story.php", data=m2data, proxies=mproxies, headers=mheaders, cookies=m2cookies) 
        else:
            r1 = requests.post("http://pikabu.ru/ajax/vote_story.php", data=m2data, headers=mheaders, cookies=m2cookies) 
        return 
class Manager(ScreenManager):
    def __init__(self, **kwargs):
        Config.set('input','mouse','mouse,multitouch_on_demand')
        Config.set('graphics','resizable',0)
        Config.set('graphics','width',800)
        Config.set('graphics','height',600)
        super(Manager, self).__init__(**kwargs)
class SelectionMenu1(Screen):
    def bConfirmOnClick(self):
        global proxyfilepath
        global proxiesFilled
        proxyfilepath=self.ids.tProxy.text
        if proxyfilepath!="":
            proxiesFilled=1
            self.manager.ids.main_menu.ids.lDone1.opacity=1
        else:
            proxiesFilled=0
            self.manager.ids.main_menu.ids.lDone1.opacity=0
        self.manager.current="Picabot"
class SelectionMenu2(Screen):
    def bConfirmOnClick(self):
        global loginfilepath
        global accountFilled
        loginfilepath=self.ids.tAccounts.text
        if loginfilepath!="":
            accountFilled=1
            self.manager.ids.main_menu.ids.lDone2.opacity=1
        else:
            accountFilled=0
            self.manager.ids.main_menu.ids.lDone2.opacity=0
        self.manager.current="Picabot"
class SelectionMenu3(Screen):
    def bConfirmOnClick(self):
        global postid
        global idFilled
        postid=self.ids.tId.text
        if postid!="":
            idFilled=1
            self.manager.ids.main_menu.ids.lDone3.opacity=1
        else:
            idFilled=0
            self.manager.ids.main_menu.ids.lDone3.opacity=0
        self.manager.current="Picabot"
class PicabotApp(App):
    def build(self):
        return Manager()
if __name__ == "__main__":
    PicabotApp().run()

