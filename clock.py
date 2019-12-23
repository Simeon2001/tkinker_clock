import tkinter as tk
import time

def clock():
    current=time.strftime("%H:%M:%S")
    label1 ["text"]=current
    root.after(1000,clock)

root=tk.Tk()
root.title('clock')
label1=tk.Label(root,font="Times 50",bg="dark blue",fg="green")
label1.grid(row=20,column=30)
label2=tk.Label(root, text="reverse engineered by Cisco",bg="dark blue",fg = "red",font = "Times 10")
label2.grid(row=40,column=30)
clock()
root.mainloop()