import customtkinter as ctk

win = ctk.CTk()
win.geometry('600x250')
frame = ctk.CTkFrame(win)
frame.grid(side='top',expand=True,fill='both')
lbl = ctk.CTkLabel(frame,text='Enter your Password',font=('Helvetica',20))
lbl.grid(pady=20)

