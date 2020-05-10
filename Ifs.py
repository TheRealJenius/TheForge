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