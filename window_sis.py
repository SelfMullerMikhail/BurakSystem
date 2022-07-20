from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from DBUtils.DBHelper import DBHelper
from Widgets.listWidget import listWidget
from Widgets.tableWidget import tableWidget
app=None;
dbHelper = DBHelper()
Window.maximize()
class AppWithKivy(App):
    def on_addorder(self,widget,selected):
        if self.selectedTable is not None:
            self.order_list.add_order(selected.dataObj)

    def on_select_table(self,widget,selected):
        self.selectedTable=selected
        self.order_list.set_table(selected)

    def build(self):
        self.title="Burak's App"
        self.width=1000
        self.selectedTable=None
        self.root = GridLayout(cols=3,orientation='lr-tb',spacing=0)
        self.all_drinks=dbHelper.get_all_drinks()
        self.drinks_widget = listWidget(self.all_drinks,False,size_hint_x=None, width=700)
        self.drinks_widget.bind(on_addorder=self.on_addorder)
        
        self.tables_widget = listWidget(dbHelper.get_all_tables(),True,size_hint_x=None, width=700)
        self.tables_widget.bind(on_addorder=self.on_select_table)


        self.order_list=tableWidget(self.all_drinks)

        self.root.add_widget(self.drinks_widget)
        self.root.add_widget(self.order_list)
        self.root.add_widget(self.tables_widget)
        return self.root
    
if __name__=='__main__':
    AppWithKivy().run();
