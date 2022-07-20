from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from DBUtils.DBHelper import DBHelper
from Widgets.listWidget import listWidget
from Widgets.tableWidget import tableWidget

app=None;
dbHelper = DBHelper()

class AppWithKivy(App):
    def on_addorder(self,widget,selected):
        if self.selectedTable is not None:
            self.order_list.add_order(selected.dataObj)

    def on_select_table(self,widget,selected):
        self.selectedTable=selected
        self.order_list.set_table(selected)

    def build(self):
        self.title="Burak's App"
        self.selectedTable=None
        self.root = GridLayout(cols=3,orientation='lr-tb',spacing=0)
        self.all_drinks=dbHelper.get_all_drinks()
        self.drinks_widget = listWidget(self.all_drinks,size_hint_x=None, width=700)
        self.drinks_widget.bind(on_addorder=self.on_addorder)
        self.root.add_widget(self.drinks_widget)
        
        self.tables_widget = listWidget(dbHelper.get_all_tables(),size_hint_x=None, width=500)
        self.tables_widget.bind(on_addorder=self.on_select_table)
        self.root.add_widget(self.tables_widget)


        self.order_list=tableWidget(self.all_drinks)
        self.root.add_widget(self.order_list)
        return self.root
    
if __name__=='__main__':
    AppWithKivy().run();
