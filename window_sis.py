from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from DBUtils.DBHelper import DBHelper
from Widgets.drinksWidget import drinksWidget
from Widgets.tableWidget import tableWidget

app=None;
dbHelper = DBHelper()
class AppWithKivy(App):
    def build(self):
        self.root = GridLayout(cols=3,orientation='tb-lr')
        self.drinks_widget = drinksWidget(dbHelper.get_all_drinks())
        self.root.add_widget(self.drinks_widget,index=1)
        self.root.add_widget(tableWidget(),index=1)
        return self.root
    
    def add_order(self,button):
        print(button)

if __name__=='__main__':
    AppWithKivy().run();
