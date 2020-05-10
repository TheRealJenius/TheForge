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
    
perm ('Ready to try: ') #calls the perm function


def minmax (items):
    return min(items), max(items)

print(minmax([54,65,13,76,23,16,11,61,64])) #the values need to be written in the square brackets to be taken as one variable, not many seperate ones, this is also known Tuple unpacking
