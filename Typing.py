from tkinter import *
from ui import UserInterface
from words_manager import WordsManager
from my_user import User
from my_timer import Timer
from words_calculator import Calculator 


root = Tk()

wm = WordsManager()
user = User()
timer = Timer()
calc = Calculator()

ui = UserInterface(root, wm, user, timer, calc)


root.mainloop()


