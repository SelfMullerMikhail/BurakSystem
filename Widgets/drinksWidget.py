from distutils.command.build import build
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class drinksWidget(ScrollView):
    def __init__(self, drinks,**kwargs):
        super().__init__(**kwargs)
        if kwargs.width is not None:
            self.size = (kwargs.width,300)
        self.build()
        self.refresh_drinks(drinks)

    def build(self):
        self.drinks_container = StackLayout(orientation='tb-lr')
        self.add_widget(self.drinks_container)

    def refresh_drinks(self,drinks):
        self.drinks_container.clear_widgets()
        for drink in drinks:
            self.drinks_container.add_widget(Button(text=drink[1],size_hint=(1,None), on_press=lambda x: self.add_order(x)))