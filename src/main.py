# Library and madules
from dhooks import Webhook
from tkinter import messagebox


def send(webhook:Webhook,message:str,embed=None):
    try:
        webhook.send(message,embed=embed)
        messagebox.showinfo("Message sended succesfully !")
    except Exception as error :
        messagebox.showerror("ERROR",f"{error}")




if __name__ == "__main__":
    pass