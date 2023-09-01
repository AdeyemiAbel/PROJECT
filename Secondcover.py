import customtkinter as ctk
from PIL import Image

def new_window():
    window = ctk.CTkToplevel()
    canvas = ctk.CTkCanvas(window,height=1000,width=1000)
    canvas.pack()

if __name__=="__main__":
    window2 = ctk.CTk()
    window2.title('VoteStream')
    canvass = ctk.CTkCanvas(window2,height=1000,width=1000)
    canvass.pack()

    btn = ctk.CTkButton(window2,text='Click me',bg_color='Green',fg_color='Yellow',command=lambda:new_window())
    btn.pack()

    window2.mainloop()