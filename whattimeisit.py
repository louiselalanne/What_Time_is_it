from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime 
import pytz 
import time

root=Tk()
root.geometry("400x400")
clock_img = ImageTk.PhotoImage(Image.open("clock.png"))

#----------------BR

brasil_label = Label(root, text="Brazil")
brasil_label.place(relx=0.2, rely=0.05, anchor=CENTER)

br_clock = Label(root)
br_clock["image"]=clock_img
br_clock.place(relx=0.2, rely=0.35, anchor=CENTER)

br_time = Label(root)
br_time.place(relx=0.2, rely=0.65, anchor=CENTER)

#-------------Ale

germany_label = Label(root, text="Germany / Berlin")
germany_label.place(relx=0.7, rely=0.05, anchor=CENTER)

gr_clock = Label(root)
gr_clock["image"]=clock_img
gr_clock.place(relx=0.7, rely=0.35, anchor=CENTER)

gr_time = Label(root)
gr_time.place(relx=0.7, rely=0.65, anchor=CENTER)

class Germany():
    def times(self):
        hora = pytz.timezone('Europe/Berlin')
        local_time = datetime.now(hora)
        conversao = local_time.strftime("%H:%M:%S")
        gr_time["text"] = "Time: " + conversao
        gr_time.after(200, self.times)

class Brazil():
    def times(self):
        hora = pytz.timezone('Brazil/DeNoronha')
        local_time = datetime.now(hora)
        conversao = local_time.strftime("%H:%M:%S")
        br_time["text"] = "Time: " + conversao
        br_time.after(200, self.times)

obj_br = Brazil()
obj_gr = Germany()

br_btn = Button(root, text="Show Time", command=obj_br.times)
br_btn.place(relx=0.2, rely=0.8, anchor=CENTER)
gr_btn = Button(root, text="Show Time", command = obj_gr.times)
gr_btn.place(relx=0.7, rely=0.8, anchor=CENTER)

root.mainloop()