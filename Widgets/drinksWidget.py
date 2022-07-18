from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class displayWidget(Button):
    def __init__(self,obj, **kwargs):
        super().__init__(**kwargs)
        self.dataObj = obj
        self.text = obj[1]

class drinksWidget(ScrollView):
    def __init__(self, drinks,**kwargs):
        super().__init__(**kwargs)
        self.build()
        self.refresh_drinks(drinks)

    def build(self):
        self.drinks_container = GridLayout(orientation='lr-tb',cols=3)
        self.add_widget(self.drinks_container)

    def refresh_drinks(self,drinks):
        self.drinks_container.clear_widgets()
        for drink in drinks:
            self.drinks_container.add_widget(displayWidget(drink,size_hint=(1,None), on_press=lambda x: self.add_order(x)))

    def add_order(self,button):
        print(button.text)