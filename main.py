"""
Formatron
Fleserig73
"""
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import pyperclip
import time
root = ctk.CTk()
root.title("Formatron")
root.geometry("800x400")
root.iconphoto(False, tk.PhotoImage(file='formatron.png'))
root.resizable(False, False)
result = ""

def beautify():
    global ctext, result
    result = textbox.get(1.0, "end")
    canvas.itemconfigure(ctext, text=result)

def minify():
    global ctext, result
    result = textbox.get(1.0, "end")
    canvas.itemconfigure(ctext, text=result)

def copy(event):
    global result
    pyperclip.copy(result)
    #animation
    copyanim = Image.open("copyanim.png")
    for i in range(1, 1000, 12):
        time.sleep(0.0001)
        copyanim2=copyanim.resize((i, i))
        copyanim2=ImageTk.PhotoImage(copyanim2)
        canvas.create_image(event.x, event.y, image=copyanim2)
        root.update()
    
def enter(event):
    global imge_copy, copyi
    imge_copy = canvas.create_image(260,10, image=icopy, anchor="nw")

def leave(event):
    global imge_copy
    canvas.delete(imge_copy)

textbox = ctk.CTkTextbox(root, width=300, height=300)
textbox.place(x=50, y=50)

b_beautify = ctk.CTkButton(root, text="Beautify", command=beautify, width=1, fg_color="#0015CA", hover_color="#001597")
b_beautify.pack(pady=50)

b_minify = ctk.CTkButton(root, text="Minify", command=minify, width=1, fg_color="#9200C6", hover_color="#920095")
b_minify.pack()

bg_logo=Image.open('formatron.png')
bg_logo=bg_logo.resize((300, 300))
bg_logo=ImageTk.PhotoImage(bg_logo)

icopy = tk.PhotoImage(file="copy.png")

canvas = tk.Canvas(root, width=300, height=300, background='#000000')
canvas.place(x=450, y=50)
canvas.create_image(0,0, image=bg_logo, anchor="nw")
ctext = canvas.create_text(10, 10, text=result, fill="white", anchor="nw")

canvas.bind('<Enter>', enter)
canvas.bind('<Leave>', leave)
canvas.bind('<Button-1>', copy)


root.mainloop()