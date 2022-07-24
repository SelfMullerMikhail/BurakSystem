class switch_tab():
    tab = int
    def got_tab(self):
        global tab
        return tab

    def switch_tab(self, number):
        print("switch is work!")
        global tab
        tab = number
