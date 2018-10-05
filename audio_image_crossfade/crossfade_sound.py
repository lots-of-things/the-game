import sounddevice as sd
import numpy as np
from PIL import Image, ImageTk
import time
import tkinter as tk

stream = sd.InputStream()
stream.start()

root = tk.Tk()
new_img = Image.open('staticy_sized.jpg')
photo = ImageTk.PhotoImage(new_img)
image_label = tk.Label(root, image=photo)
image_label.pack()

def picapture():
    global image_label, root, stream
    alpha = min(np.abs(stream.read(10000)[0]).mean()*10,1)
    black = Image.open('desk_central_park.jpg')
    white = Image.open('staticy_sized.jpg')
    new_img2 = Image.blend(white,black,alpha)
    new_photo = ImageTk.PhotoImage(new_img2)
    image_label.configure(image=new_photo)
    image_label.image = new_photo
    root.after(100, picapture)
    
picapture()

root.mainloop()