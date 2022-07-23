import re
from db_helper import db_helper
from tab import switch_tab
from tab import got_tab

switch_tab(1)
name = got_tab()
print(name)

switch_tab(2)
name = got_tab()

print(name)