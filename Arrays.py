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
l.reverse() # reverse arrays
print (l)
l.sort() # sort array
print (l)

number = [54,13,456,4,34,5674]
print (number)
number.sort()
print (number)