from cProfile import label
from tkinter import Label
from main_window.photosHelper import PhotoHelper
from tkinter import Frame

class UpPanel_Frame(Label):
    def __init__(self, main_window):
        super().__init__(main_window, width=400, height=3, background="grey")
        self.place(x =1, y =1)

class Cats_fone(Label):
    def __init__(self, main_window):
        # self.photo = PhotoHelper("main_window/catsPhotoMain.jpg")
        # super().__init__(main_window, width=565, height=700, image=self.photo)
        self.photo = PhotoHelper("img/catsPhotoMain.jpg")
        super().__init__(main_window, width=565, height=700, background="grey")
        self.place(x =1, y =1)

class Tables_Place(Frame):
    def __init__(self, main_window):
        super().__init__(main_window, width=580, height=650)
        self.place(x=1, y=50)


