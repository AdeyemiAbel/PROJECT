import customtkinter as ctk
from PIL import Image

splash_win = ctk.CTk()
splash_win.title('Splash Screen Example')
splash_win.geometry('700x200')
splash_win.overrideredirect(True)

splash_lbl = ctk.CTkLabel(splash_win,text='Hello world!',fg_color='green',font=('Helvetica bold', 40)).grid()

def mainWin():
    splash_win.destroy()
    win = ctk.CTk()
    win.title('Main Window')
    win.geometry('700x200')
    win_lbl = ctk.CTkLabel(win,text='Main Window', font=('Helvetica bold', 25),fg_color='red').grid()

splash_win.after(4000,mainWin)

splash_win.mainloop()