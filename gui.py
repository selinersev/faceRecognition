from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import os

window = Tk()
window.title("Face Analyze")
window.geometry('1200x800')
#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)
lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)

def clicked():
    file_path = askopenfilename()
    img = ImageTk.PhotoImage(Image.open(file_path))
    img = img.resize((250, 250), Image.ANTIALIAS)
    imglabel = Label(window, image=img)
    imglabel.grid(column=8, row=0)
    print(file_path)
btn1 = Button(window, text="Choose File", command=clicked)
btn1.grid(column=0, row=0)
btn2 = Button(window, text="Detect Face", command=clicked)
btn2.grid(column=2, row=0)
btn3 = Button(window, text="Recognize Face", command=clicked)
btn3.grid(column=4, row=0)
btn4 = Button(window, text="Face Lendmarks", command=clicked)
btn4.grid(column=6, row=0)

window.mainloop()


