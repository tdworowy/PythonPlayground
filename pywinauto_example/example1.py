"""https://pywinauto.github.io"""
from pywinauto.application import Application

# app = Application().start("E:\Program Files (x86)\SteamLibrary\steamapps\common\GemCraft Chasing Shadows\GemCraft Chasing Shadows.exe")
app = Application().start("D:\Program Files (x86)\\Notepad++\\notepad++.exe")
app.window().print_control_identifiers()
# pywinauto.findwindows.find_window(class_name="ApolloRuntimeContentWindow")
# app.window(class_name="ApolloRuntimeContentWindow").dump_tree()

# app.UntitledNotepad.menu_select("File->New")
# app.UntitledNotepad.Edit.type_keys("Test", with_spaces=True)
#TODO