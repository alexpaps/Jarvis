
import subprocess
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

def start_Jarvis(event):
    subprocess.Popen(['python', 'Jarvis.py'])

root = Tk()
root.title('My App')

# Load the background image and convert it to a PhotoImage object
bg_image = Image.open('Jarvis.png')
#J.A.R.V.I.S.png or Jarvis.png
bg_photo = ImageTk.PhotoImage(bg_image)

#The App Window size
root.geometry('500x500')

#Not changable Window size
root.resizable(False, False)

# Create a Label widget with the background image as its background
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind the <Button-1> event to the app window
root.bind('<Button-1>', start_Jarvis)

root.mainloop()
