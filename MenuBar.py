import tkinter
top=tkinter.Tk()
def hello():
    print("hello!")

menubar=tkinter.Menu(top)

filemenu = tkinter.Menu(menubar)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menubar)
editmenu.add_command(label="Undo", command=hello)
editmenu.add_command(label="Redo", command=hello)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tkinter.Menu(menubar)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)
top.wm_title("Wax")

top.config(menu=menubar)

top.mainloop()


