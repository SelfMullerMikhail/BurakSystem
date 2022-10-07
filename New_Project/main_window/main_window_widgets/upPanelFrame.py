from cProfile import label
from tkinter import Label
from main_window.photosHelper import PhotoHelper

class UpPanel_Frame(Label):
    def __init__(self, main_window):
        super().__init__(main_window, width=400, height=3, background="grey")
        self.place(x =1, y =1)

class Cats_fone(Label):
    def __init__(self, main_window):
        self.photo = PhotoHelper("main_window/catsPhotoMain.jpg")
        super().__init__(main_window, width=565, height=700, image=self.photo)
        self.place(x =1, y =1)

