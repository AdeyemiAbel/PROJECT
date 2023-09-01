import customtkinter as ctk
from PIL import Image

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("VoteStream")
    window.geometry('1400x800+0+0')

    bg_image = ctk.CTkImage(light_image=Image.open('voteimg1.png'), size=(1400,570))
    option_frame = ctk.CTkFrame(master=window,fg_color='white')
    option_frame.grid(row=0,column=0)

    bg_label = ctk.CTkLabel(master=option_frame, image=bg_image, text='')
    bg_label.grid(row=0, column=0)

    logo_image = ctk.CTkImage(light_image=Image.open('coderslogo.png'), size=(200,150))
    logo = ctk.CTkLabel(bg_label,image=logo_image, bg_color='white',text='')
    logo.grid(row=0, column=0, sticky='nw')

    about_text = ctk.CTkButton(bg_label,text='About',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    about_text.grid(row=0,column=0,padx=(1,600), pady=(80,0), sticky='ne')
    help_text = ctk.CTkButton(bg_label,text='Help',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    help_text.grid(row=0,column=0,padx=(1,500), pady=(80,0), sticky='ne')
    method_text = ctk.CTkButton(bg_label,text='Methods',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    method_text.grid(row=0,column=0,padx=(1,400),pady=(80,0), sticky='ne')
    method_var = ctk.StringVar(value="single transferable vote")
    method_combobox = ctk.CTkComboBox(bg_label,values=["single transferable vote", "Borda", "Instant runoff voting", "Condorcet", "Approval voting", "Plurality/FPTP"],width=0,variable=method_var,fg_color='black')
    method_combobox.grid(row=0,column=0,padx=(1,350),pady=(80,0),sticky='ne')
    login_btn = ctk.CTkButton(bg_label,text='Login',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    login_btn.grid(row=0,column=0,padx=(1,200), pady=(80,0), sticky='ne')
    description_header = ctk.CTkLabel(bg_label,text='We Make Online Elections Thorough and Effortless',text_color='Black',font=('Arial Bold',30),fg_color='white')
    description_header.grid(row=1,column=0,padx=(100,0))

    description_text = ctk.CTkLabel(bg_label,text='''
                        VoteStream is a secure online voting platform that makes it easy to run elections at a fraction of
                            the usual cost. We're the leading provider of ranked choice elections, which helps achieve 
                                more democratic outcomes by better representing the will of your votes.''',
                                                text_color='Black',font=('Arial',20),fg_color='white')
    description_text.grid(row=3,column=0,padx=(10,0))

   


window.mainloop()

    # opts =ctk.StringVar()
    # Label(window, textvariable=opts)
    # method_combobox = ctk.CTkComboBox(window, widget_text=opts, width=30)
    # method_combobox['values'] = ["single transferable vote", "Borda", "Instant runoff voting", "Condorcet", "Approval voting", "Plurality/FPTP"]
    # method_combobox.grid(row=0,column=0,padx=(1,350),pady=(80,0),sticky='ne')
