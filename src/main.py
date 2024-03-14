# Library and madules
from dhooks import Webhook , Embed
from tkinter import messagebox


# def send(webhook:Webhook,message:str,embed=None):
#     try:
#         if message != "":
#             if embed != None:
#                 webhook.send(message,embed=embed)
#             elif embed == None:
#                 webhook.send(message)
#         elif message == "":
#             if embed != None:
#                 webhook.send(embed=embed)

#         messagebox.showinfo("Done ✅","Contents sended succesfully !")
#     except Exception as error :
#         messagebox.showerror("ERROR",f"{error}")


class Content:
    """This class is for creating content templates
       such as message, sender's email address, embed content, etc"""


    def __init__(self,webhook_url:str,message=None,embed_title=None,embed_description=None):
        self.webhhok = Webhook(webhook_url)
        self.message = message
        self.embed_title = embed_title
        self.embed_descreption = embed_description
        self.embed = Embed(title=embed_title,description=embed_description)


    def __str__(self):
        return "Your content is : Message -> {} Webhook URL is -> {}".format(self.message,self.webhhok_url)



    def send(self):
        if self.message != "":
            if self.embed.title or self.embed.description != "":
                try:
                    self.webhhok.send(self.message,embed=self.embed)
                    messagebox.showinfo("Done ✅","Contents sended succesfully !")
                except Exception as error:
                    messagebox.showerror("ERROR",error)

            elif self.embed.title == "":
                if self.embed.description == "":
                    try:
                        self.webhhok.send(self.message)
                        messagebox.showinfo("Done ✅","Contents sended succesfully !")
                    except Exception as error:
                        messagebox.showerror("ERROR",error)
                    
        elif self.message == "":
            if self.embed.title or self.embed.description != "":
                try:
                    self.webhhok.send(embed=self.embed)
                    messagebox.showinfo("Done ✅","Contents sended succesfully !")
                except Exception as error:
                    messagebox.showerror("ERROR",error)


    

if __name__ == "__main__":
    pass