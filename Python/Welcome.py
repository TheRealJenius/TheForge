print ('Welcome to Python, Jesse ^_^')
def add(x,y):
    return x + y #+ for add, - for subtraction

print (add (4,5))

#adding as a test

def power(o,p):
    return o**p #** for power, * for multiply
print (power (3,4))

def nodec(j,k):
    return j//k #/ divide, // divide without a decimal
    return j%k #returns the remainder of the division
print(nodec(4,3))

print ("this it without \" showing " )

print("""
Testing prints
on different lines

and             indentations
"""
)
print (3* "J" + "yes")

word = "Jesse"
print(word[2]) # arrays start from 0 in python
print (word[0:3]) # from 0 to 2, excludes 3
print (word[:2]) #characters from the begining to position 2
print (word[2:]) # characters from position 2 to the end
print (word[:2] + word[2:])
print (word[-2:]) # characers from the second-last to the end

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters[3])
letters[2] = 'i'
print (letters)
letters[2:4] =[] #clearing list for position 2,3
print (letters)

'''
x = int ( input (" Please Enter a number/integer: "))
if x <0:
    x = 0
    print ("Negative changed to '0'")
elif x == 0: #elif needs to be in the same indentation as if statement
    print ('Zero')
elif x == 1:
    print ('One')
else: #else statment doesn't need to be defined, as it will be the case if all-else fails, no pun intended
    print ('More than one')
'''

a,b = 0,1
while a<100: #executes as long as the condition remains true 
    print (a, end=',') #end avoids a new line
    a,b = b, a+b

words = ['wolf', 'panda', 'whale']
for w in words:
    print (w, len(w))


''' Need to fix the below code

users = ['jesse', 'sean','william']

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

acitve_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user]=status

'''

for i in range(3, 8): # the last number denoted in range is not shown
    print (i)

for j in range (1,20,2): #the third value denotes the steps it increments or decrements by
    print (j)

q = ['Testing', 'tested', 'try', 'tried']
for i in range(len(q)):
    print(i,q[i])

print(sum(range(4))) #1+2+3+4
print(list(range(4))) # to get a list from a range

#a better to explain the above is for every value, in the list/range print statement
r = [1,5,3,7,8]
for i in r:
    print (r)


for n in range(2,12):
    for x in range(2,n):
        if n % x == 0:
            print (n,'equals', x, '*', n//x)
            break #without the break statement the if satment would loop while in the for statment, this allows the for stament to visit the next value in range
        else:
            #starts if a factor wasn't found
            print (n, 'is a prime number')
for num in range(2,19):
    if num % 2 == 0:
        print ("Here's an even number ", num)
        continue
    print ("Here's a normal number ", num)
def testlog(*arg):
    pass #skips running this function

def perm (prompt, retries=4, remainder ='please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n','no','nop','nope') :
            return False
        retries = retries - 1
        if retries <0:
            raise ValueError('invalid response')
        print (remainder)
    
# perm ('Ready to try: ') #calls the perm function


def minmax (items):
    return min(items), max(items)

print(minmax([54,65,13,76,23,16,11,61,64])) #the values need to be written in the square brackets to be taken as one variable, not many seperate ones, this is also known Tuple unpacking

named = ';'.join(['User 1', 'User 2','User 3', 'User 4'])
print(named)
named = named.split(';')
print (named)


l = 'Mary had a little lamb, a little lamb'.split()
print (l)
t = l.index('little') #returns the postion of the word in the list created as l
print(t)
c = l.count('a') #counts how many times a exists in the list
print (c)
print('Mary' in l) #returns a true or false value
print ('little' not in l)
del l[3] #removes by position
print (l)
l.remove ('Mary') #removes by value
print (l)
l.insert(4,'very') # insert a value into the string position
print (l)
l = l.reverse
print (l)
l=l.sort()
print (l)

number = [54,13,456,4,34,5674]
print (number)
number = number.sort
print (number)






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





""" To create anything in kinter is a two step process. C
 1. Define the thing and create it.
 2. Put the created label widget on the screen
"""
# Here I am creating a Label widget
#mylabel = Label(root, text="Hello World!")


""" The Pack manager literally packs widgets into rows or columns.
All widgets are packed into one master widget.
This puts the label widget onto the screen.
"""
#mylabel.pack() 

""" We now need to create an event loop.
In an GUI, it's always looping constantly to understand what is happening.
As it is looping, you may move the mouse, since it loops, the program notices the change.
A program ends when the loop ends.
root.mainloop() runs the main look of root which is TK(), so essentially runs the main loop on TK()

"""
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


'''
from Tkinter import *  - imports every exposed object in Tkinter into your current namespace. 
import Tkinter  - imports the "namespace" Tkinter in your namespace 
import Tkinter as tk -  does the same as above, but "renames" it locally to 'tk' to save typing + allows it to be called within a class

example:
Let's say we have a module foo, containing the classes A, B, and C.
Then import foo gives you access to foo.A, foo.B, and foo.C.
When you do import foo as x you have access to those too, but under the names x.A, x.B, and x.C. from foo import * will import A, B, and C directly in your current namespace, so you can access them with A, B, and C.
There is also from foo import A, C wich will import A and C, but not B into your current namespace.
You can also do from foo import B as Bar, which will make B available under the name Bar (in your current namespace).
So generally: when you want only one object of a module, you do from module import object or from module import object as whatiwantittocall.
When you want some modules functionality, you do import module, or import module as shortname to save you typing.

from module import * is normally discouraged, as we may accidentally shadow ("override") names, and may lose track which objects belong to wich module.
'''
'''
import tkinter as tk #Need to import tkinter as tk - so it references the functions such as Frame, etc.

LargeFONT= ("Verdana", 12)


class Notes(tk.Tk):  #Need to set it as a calss so the functions can all be called
    ''
    the items in the brackets allow you to inherit attributes from another class , a class can be created without it
    ''
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

'''