Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
... from PIL import ImageTk, Image
... 
... root = Tk()
... root.title("my GUI")
... root.geometry("250x150")
... img = ImageTk.PhotoImage(Image.open(r'C:\Users\devil\OneDrive\Desktop\download.JPEG'))
... panel = Label(root, image = img)
... panel.pack(side = "bottom", fill = "both", expand = "yes")
