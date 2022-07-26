class Switch_tab():
    def got_tab(self):
        global tab
        print(f"switcher.got_tab: {tab}")
        return tab

    def switch_tab(self, number):
        global tab
        tab = number
        print(f"switcher.switch_tab: {tab}")

switcher = Switch_tab()
