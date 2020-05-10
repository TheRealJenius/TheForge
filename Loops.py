
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
