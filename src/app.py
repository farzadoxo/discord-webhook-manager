# Library and madules
from tkinter import Tk as Tk
from tkinter import Button , Text , Label , LabelFrame , colorchooser
from dhooks import Webhook , Embed
from main import send

# Varables
discord_color = '#36393e'
burple = '#7289da'

# Definition Window and set properties
window = Tk()

window.title("Webhook Manager (0.2)")
window.iconbitmap('media\\icon.ico')
window.geometry('600x550')
window.resizable(False,False)
window.configure(bg=discord_color)
window.eval('tk::PlaceWindow . center')


# Definition Components

header_label = Label(window,text="Discord Webhook manager",fg=burple,font=("Arial",18,'bold'),bg=discord_color)
# - webhook url
webhook_url_label = Label(window,text="Webhook URL :",bg=discord_color,fg='white')
webhook_url_textbox = Text(window,width=62,height=2)
# - message
message_groupbox = LabelFrame(text="Content",width=500,height=195,bg=discord_color,fg='white')
message_label = Label(window,text="Message :",bg=discord_color,fg='white')
message_textbox = Text(window,height=10,width=50)
message_clear_button = Button(window , text="Clear",bg='red',fg='white',width=6,height=1,command=lambda:message_textbox.delete('1.0', 'end-1c'))
send_button = Button(window , text="SEND",bg='green',fg='white',cursor='hand2',
                      command=lambda:send(
                          webhook=Webhook(url=webhook_url_textbox.get("1.0",'end-1c')),
                          message=message_textbox.get("1.0",'end-1c'),
                          embed=Embed(
                              title=embed_title_textbox.get("1.0",'end-1c'),
                              description=embed_description_textbox.get("1.0",'end-1c'),
                              color=0xffffff
                          )))

# - embed
embed_groupbox = LabelFrame(text="Embed",width=500,height=195,bg=discord_color,fg='white')
embed_title_label = Label(window,text="Title :",bg=discord_color,fg='white')
embed_title_textbox = Text(window,width=30,height=1)
embed_description_label = Label(window,text="Descreption :",bg=discord_color,fg='white')
embed_description_textbox = Text(window,width=50,height=8)



# Locating objects on window

header_label.place(x=5,y=2)
# - webhook url
webhook_url_label.place(x=5,y=50)
webhook_url_textbox.place(x=93,y=55)
# - message
message_groupbox.place(x=5,y=92)
message_label.place(x=15,y=110)
message_textbox.place(x=80,y=110)
message_clear_button.place(x=17,y=150)
# - embed
embed_groupbox.place(x=5,y=300)
embed_title_label.place(x=55,y=320)
embed_title_textbox.place(x=95,y=320)
embed_description_label.place(x=15,y=350)
embed_description_textbox.place(x=95,y=350)
# - send
send_button.place(x=550,y=510)


# Run window
window.mainloop()