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


a,b = 0,1
while a<100: #executes as long as the condition remains true 
    print (a, end=',') #end avoids a new line
    a,b = b, a+b

words = ['wolf', 'panda', 'whale']
for w in words:
    print (w, len(w))
