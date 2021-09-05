from tkinter import *
Window = Tk()
Window.title("Paint Application")
Window.geometry("500x350")
def paint(event):
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x-3), (event.y-3)
    x2, y2 = (event.x+3), (event.y+3)
    color = "black"
    # display the mouse movement inside canvas
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
# create canvas
wn=Canvas(Window, width=500, height=350, bg='white')
# bind mouse event with canvas(wn)
wn.bind('<B1-Motion>', paint)
wn.pack()
Window.mainloop()

