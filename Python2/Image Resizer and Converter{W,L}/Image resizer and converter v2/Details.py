from Tkinter import *
#from ttk import *
from PIL import Image, ImageTk
trans_color = '#FFFFFE'
root = Tk()
img = ImageTk.PhotoImage(Image.open(raw_input("Name of image ~ ")))
img_label = Label(root, image=img)
img_label.pack()
img_label.img = img  # PIL says we need to keep a ref so it doesn't get GCed
root.update()
overlay = Toplevel(root)
print 'image geometry X is...', root.geometry()
geometry = '{}x{}+{}+{}'.format(root.winfo_width(), root.winfo_height(),
    root.winfo_rootx(), root.winfo_rooty())
print 'image geometry Y is.....',geometry
overlay.geometry(geometry)
overlay.overrideredirect(1)
overlay.wm_attributes('-transparent', trans_color)
overlay.config(background=trans_color)

Label = Label(overlay, text='Image Details')
Label.config(background=trans_color)
Label.pack()
root.mainloop()
