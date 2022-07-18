from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from DBUtils.DBHelper import DBHelper
from Widgets.drinksWidget import drinksWidget
from Widgets.tableWidget import tableWidget

app=None;
dbHelper = DBHelper()
class AppWithKivy(App):
    def build(self):
        self.title="Burak's App"
        self.root = GridLayout(cols=3,orientation='tb-lr',spacing=10)
        self.drinks_widget = drinksWidget(dbHelper.get_all_drinks(),size_hint_x=None, width=700)
        self.tables_widget = drinksWidget(dbHelper.get_all_tables(),size_hint_x=None, width=500)
        self.root.add_widget(self.drinks_widget)
        self.root.add_widget(self.tables_widget)
        self.root.add_widget(tableWidget())
        return self.root
    
    def add_order(self,button):
        print(button)

if __name__=='__main__':
    AppWithKivy().run();
