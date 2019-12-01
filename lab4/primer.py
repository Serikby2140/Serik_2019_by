from tkinter import *
root = Tk()

c = Canvas(root, width=200, height=200, bg='lightgrey')
c.pack()

c.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
c.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
c.create_arc(10, 10, 190, 190, start=270, extent=25, fill='orange')
c.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
c.create_arc(10, 10, 190, 190, start=50, extent=180, style=ARC, outline='darkblue', width=5)

c.create_text(100, 100, text="Hello World,\nPython\nand Tk",
                justify=CENTER, font="Verdana 14")
c.create_text(200, 200, text="About this",
                anchor=SE, fill="grey")

root.mainloop()