from tkinter import *
from Interface import *


fenetre = Tk()
fenetre.geometry("500x500")
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
