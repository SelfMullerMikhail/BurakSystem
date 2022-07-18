from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from DBUtils.DBHelper import DBHelper
from Widgets.drinksWidget import drinksWidget

app=None;
dbHelper = DBHelper()
class AppWithKivy(App):
    def build(self):
        self.root = GridLayout(cols=3)
        self.drinks_widget = drinksWidget(dbHelper.get_all_drinks(),width=300)
        self.root.add_widget(self.drinks_widget,index=0)
        return self.root
    
    def add_order(self,button):
        print(button)

if __name__=='__main__':
    AppWithKivy().run();
