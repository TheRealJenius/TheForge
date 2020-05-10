# And so it begins

"""
Things to do:
- Define Functions required
    - Enter input
    - Display input as output
    - Delete input
    - Copy input
    - Paste input
- Create a GUI
    - TKinter seems to be the default a good place to start
- Create Menus
    - File
    - Edit
    - About
- Time and date package
    - Save as a file that can be accessed
    - Save as a thumbnail
"""



# https://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/
# https://www.tutorialspoint.com/develop-notepad-using-tkinter-in-python
# https://www.geeksforgeeks.org/make-notepad-using-tkinter/


'''
frame1 = tk.Frame()
frame2 = tk.Frame()
frame1.pack(side='top')  # side='top' is default
frame2.pack(side='top')
# these widgets go into frame1
label = tk.Label(frame1, text="Enter your name:")
entry = tk.Entry(frame1)
label.pack(side='top')
entry.pack(side='top')
# these widgets go into frame2
btn1 = tk.Button(frame2, text='button1')
btn2 = tk.Button(frame2, text='button2')
btn3 = tk.Button(frame2, text='button3')
btn1.pack(side='left')
btn2.pack(side='left')
btn3.pack(side='left')
'''

'''
import tkinter from tkinter.constants import * 
tk = tkinter.Tk() 
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) 
frame.pack(fill=BOTH,expand=1) 
label = tkinter.Label(frame, text="Hello, World") 
label.pack(fill=X, expand=1) 
button = tkinter.Button(frame,text="Exit",command=tk.destroy) 
button.pack(side=BOTTOM) 
tk.mainloop()

'''
#Tcl = tool command language
#Tk = Tool Kit

#text.grid() #grid doesn't populate without ()

#############################################################################################################################

# Coding begins
# from Tkinter import *
# '*' Imports everything, everything is a widget in tkinter
# root = Tk() # Creates the origin 'window' widget or the root widget, this has to be the first thing. - This is the label widget.
'''
TextArea=Text(root) #TextArea displays text
MenuBar = Menu(root)
MenuFile = Menu(root, tearoff = 0)  #tearoff allows the menu to open a seperate window within the main window to display the attributes defined
MenuEdit = Menu(root, tearoff = 0)  
'''

import tkinter as tk #Need to import tkinter as tk - so it references the functions such as Frame, etc.

LargeFONT= ("Verdana", 12)


class Notes(tk.Tk):  #Need to set it as a calss so the functions can all be called
    '''
    the items in the brackets allow you to inherit attributes from another class , a class can be created without it
    '''
    def __init__(self,*args, **kwargs): #sets the code that loads first, self is a parameter that is normally implied and can be changed if required, it's good practice to leave it as self
        # *args = arguments = variables
        # **kwargs = keyword argumemts = e.g. dictionaires
        # you could essentially write the above as (self,*,**)
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self) #frame defines the window
        # pack esentially just places an element on the window without any direction or organisation
        # grid is the opposite and allow you to decide where items go
        container.pack(side="top", fill = "both", expand = True)
        # side is a generic direction
        # fill will fill in the space we have set for the pack
        # expand will check if there is anymore whitespace on the window, to allow the container to expand within the space
        container.grid_rowconfigure(0, weight=1) #0 sets the minimu size, weight defines the priority it increments by
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} #empty dictionary

        frame = StartPage(container, self)

        self.frames[StartPage] = frame
        
        frame.grid(row=0, column = 0, sticky = "nsew") #North South East West = nsew, it defines alignment - i.e. ew will strecth it in the centre

        self.show_frame(StartPage)

    def show_frame(self,cont): 
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "Start Page", font = LargeFONT)
        label.pack(pady=10, padx=10)

#when you call upon a class it is going to return an object and we'll assign that object to a variable and call the variable to carry out functions

Application = Notes()

Application.mainloop()
# creating a quit button instance below - for testing
quitButton = Button(self, text = "Quit", command = self.client_exit) # Button is part of tkinter, client_exit hasn't been defined yet
quitButton.place(x=0, y=0) # adds the button to the window; It starts from the upper left hand side
# at this point it is a good idea to start noting down the size of the button, he geometry pointed out below
    
def client_exit(self): # defining the quit function doesn't neccesarily need to happen as it is just one line, but has been added here as the prgoram grows
    exit() # built in function in python
