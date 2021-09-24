import pyshorteners
from tkinter import *
r = Tk()
r.title("url shortner")
r.geometry("400x100")
r.config(bg="yellow")

def url_shortner():
    d = pyshorteners.Shortener().tinyurl.short(url.get())
    shortenedurl.set(d)
url = StringVar()
shortenedurl = StringVar()
Label(r,text="Enter url here:",bg="yellow").grid(row=0,column=0)
Entry(r,textvariable=url,fg="blue",width=40,bg="pink").grid(row=0,column=1,pady=5)
Button(r,text="click",command=url_shortner,bg="red").grid(row=1,column=1)
Entry(r,textvariable=shortenedurl,fg="blue",width=40,bg="pink").grid(row=2,column=1,pady=5)
r.mainloop()
