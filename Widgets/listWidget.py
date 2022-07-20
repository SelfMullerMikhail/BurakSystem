import uuid
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.splitter import Splitter;
from kivy.graphics import *

class displayWidget(Button):
    def __init__(self,obj, **kwargs):
        super().__init__(**kwargs)
        self.dataObj = obj
        self.text = obj[1]
        self.set_selected(False);
        self.guid=uuid.uuid4().hex

    def set_selected(self,isActive):
        if len(self.dataObj)>2:
            return
        if isActive:
            self.background_color= (0,1,0,1)
        else:
            self.background_color= (1,1,1,1)

    def renew_guid(self):
        self.guid=uuid.uuid4().hex
            

class listWidget(Splitter):
    def __init__(self, drinks,isRight,**kwargs):
        super(listWidget,self).__init__(**kwargs)
        self.register_event_type('on_addorder')
        self.build()
        self.refresh_drinks(drinks)
        self.sizable_from=("right","left")[isRight==True]
        self.strip_size="7pt"
        self.selected=None
        

    def on_addorder(self,x):
        pass

    def throw_event(self,x):
        if self.selected is not None:
            self.selected.set_selected(False)
        self.selected=x
        self.selected.set_selected(True);
        self.dispatch('on_addorder',x)

    def build(self):
        self.drinks_container = GridLayout(orientation='lr-tb',cols=3)
        self.add_widget(self.drinks_container)

    def refresh_drinks(self,drinks):
        self.drinks_container.clear_widgets()
        for drink in drinks:
            self.drinks_container.add_widget(displayWidget(drink,size_hint=(1,None), on_press=lambda x: self.throw_event(x)))
