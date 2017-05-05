#START CODE SAVED FOR LATER
#
#switchmenu = tkinter.Menu(menubar)
#switchmenu.add_command(label="View Mode", command=hello)
#switchmenu.add_command(label="Write Mode", command=hello)
#filemenu.add_cascade(label="Switch To...", menu=switchmenu)
#
#END CODE SAVED FOR LATER

from tkinter import *

root=Tk("Wax")

root.wm_title("Wax")

#VARIABLES
tabwidth = 20
#END VARIABLES

#FUNCTIONS
def hello():
    print("hello!")
#END FUNCTIONS

#TOP MENU
writemenubar=Menu(root)

filemenu = Menu(writemenubar)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_command(label="Save As", command=hello)
filemenu.add_command(label="Print Preview", command=hello)
filemenu.add_command(label="Print Options", command=hello)
filemenu.add_command(label="Print", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
writemenubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(writemenubar)
editmenu.add_command(label="Undo", command=hello)
editmenu.add_command(label="Redo", command=hello)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
writemenubar.add_cascade(label="Edit", menu=editmenu)

insertmenu = Menu(writemenubar)
insertmenu.add_command(label="Image", command=hello)
insertmenu.add_command(label="Formula", command=hello)
insertmenu.add_command(label="Special Character", command=hello)
writemenubar.add_cascade(label="Insert", menu=insertmenu)
writemenubar
viewmenu = Menu(writemenubar)
viewmenu.add_command(label="Write Mode")

helpmenu = Menu(writemenubar)
helpmenu.add_command(label="About", command=hello)
writemenubar.add_cascade(label="Help", menu=helpmenu)
#END TOP MENU 

#QUICK ACCESS

#END QUICK ACCESS

#FILE PANE
filepane = Frame(root)
placeholderfile = Label(filepane, text="FUCK")
placeholderfile.grid()
filepane.grid(column = 0)
#END FILE PANE

#TASK PANE
taskpane = Frame(root)
placeholdertask = Label(taskpane, text="FUCK")
placeholdertask.grid()
taskpane.grid(column = 1)
#END TASK PANE

#WRITE PANE
writepane = Frame(root)

header = Entry(writepane)
header.grid(column = 0)

subheader = Text(writepane)
subheader.grid(column = 0, ipadx = tabwidth)

note = Text(writepane)
note.grid(column = 0, ipadx = tabwidth*2)

writepane.grid(column = 2, ipadx = tabwidth*3)
#END WRITE PANE

root.config(menu=writemenubar)


root.mainloop()
#CLASS DEFINITIONS
#FILE CLASS
#class writecontent(root.Frame):
#	def __init__(self, root):

#END FILE CLASS
#TASK CLASS
#class writecontent(root.Frame):
#	def __init__(self, root):

#END TASK CLASS
#WRITECONTENT CLASS
#class writecontent(root.Frame):
#	def __init__(self, root):

#END WRITECONTENT CLASS
#END CLASS DEFINITIONS