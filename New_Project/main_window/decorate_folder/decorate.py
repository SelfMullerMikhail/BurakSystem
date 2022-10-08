from main_window.decorate_folder.labels import Label_info

class Decorate_main_window():
    def __init__(self, window, version):
        self.version = version
        main_window = Label_info(window, self.version, 1000, 670)