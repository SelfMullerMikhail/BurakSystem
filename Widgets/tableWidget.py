from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.graphics import *

class tableWidget(ScrollView):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'tb-lr'
    def draw_background(widget, prop):
      with widget.canvas:
        Color(rgba=[1,0,0,1])
        Rectangle(pos=self.pos, size=self.size)
    self.bind(size=draw_background)
    self.bind(pos=draw_background)
    self.add_widget(Button(text='Button 1', size_hint=(1, None), height=100))