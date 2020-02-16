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


