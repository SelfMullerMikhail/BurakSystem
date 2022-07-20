from cgitb import text
import kivy
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import *
from DBUtils.DBHelper import DBHelper

class orderWidget(BoxLayout):
  __dbHelper=DBHelper();
  def __init__(self,order,rowid,quantity, **kwargs):
    super(orderWidget,self).__init__(**kwargs)
    self.orientation='horizontal'
    self.size_hint=(1,None)
    self.height=80
    self.order=order
    self.rowid=rowid
    self.quantity=quantity

    self.name_label=Label(text=order[1],size_hint=(.4,1))
    self.quantity_label=Label(text=str(self.quantity),size_hint=(.2,1))
    self.add_button=Button(text="Add",size_hint=(.2,1),on_press=lambda x:self.increase_quantity())
    self.remove_button=Button(text="Remove",size_hint=(.2,1),on_press=lambda x:self.increase_quantity(False))

    self.add_widget(self.name_label)
    self.add_widget(self.quantity_label)
    self.add_widget(self.add_button)
    self.add_widget(self.remove_button)

  def increase_quantity(self,increase=True):
    if increase:
      self.quantity+=1
    else:
      self.quantity-=1
      if(self.quantity==0):
        self.__dbHelper.remove_order(self.rowid)
        self.parent.parent.parent.get_total()
        self.parent.remove_widget(self)
        return
    self.__dbHelper.update_quantity(self.rowid,self.quantity)
    self.quantity_label.text=str(self.quantity)
    self.parent.parent.parent.get_total()

  def get_total(self):
    return self.quantity*self.order[2]

class tableWidget(GridLayout):
  __dbHelper=DBHelper();
  def __init__(self,drinks, **kwargs):
    super(tableWidget,self).__init__(**kwargs)
    self.all_drinks=drinks
    self.rows=4
    self.table_label=Label(text="TEXT",size_hint=(1,None),height=100)
    self.add_widget(self.table_label)
    
    self.orders_scroll=ScrollView(size_hint=(1,1))
    self.add_widget(self.orders_scroll)

    self.order_box=StackLayout(orientation='lr-tb')
    self.orders_scroll.add_widget(self.order_box)
    self.total_label=Label(text="TOTAL", size_hint=(1, None), height=100,font_size='60sp')
    self.add_widget(self.total_label)
    self.add_widget(Button(text='Clear', size_hint=(1, None), height=100,on_press=lambda x:self.close_table()))

    self.selected_table=None

  def set_table(self,table):
    if self.selected_table == table:
      return;
    self.selected_table=table
    self.table_label.text=table.dataObj[1]
    self.order_box.clear_widgets();
    self.datas=self.__dbHelper.get_all_orders(self.selected_table.guid)
    for data in self.datas:
      order=next((x for x in self.all_drinks if x[0]==data[2]),None)
      if order is not None:
        self.check_add_or_increase(order,data[0],data[4])
    self.get_total()

  def add_order(self,order):
    for child in self.order_box.children[:]:
      if child.order==order:
        child.increase_quantity()
        self.get_total()
        return
    rowid=self.__dbHelper.add_order(order[0],self.selected_table.dataObj[0],self.selected_table.guid)
    self.check_add_or_increase(order,rowid)

  def get_total(self):
    total=0
    for child in self.order_box.children[:]:
      total+=child.get_total()
    self.total_label.text=str(total)

  def check_add_or_increase(self,order,rowid=0,quantity=1):
    for child in self.order_box.children[:]:
      if child.order==order:
        child.increase_quantity()
        self.get_total()
        return
    self.order_box.add_widget(orderWidget(order,rowid,quantity))
    self.get_total()

  def remove_order(self,order):
    self.__dbHelper.remove_order(order)

  def close_table(self):
    if self.selected_table is None:
      return
    self.selected_table.renew_guid()
    self.order_box.clear_widgets()
    self.get_total();

  def new_table(self):
    if self.selected_table is None:
      return
    self.selected_table.renew_guid()
    self.order_box.clear_widgets()
    self.get_total();
