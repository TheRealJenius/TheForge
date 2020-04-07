names =  list(input("Please enter names seperated by commas: ").split(","))# get and process input for a list of names
assignments = list(input("Please enter assignment count seperated by commas: ").split(",")) # get and process input for a list of the number of assignments
grades = list(input("Please enter grades seperated by commas: ").split(",")) # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for n,a,g in zip(names,assignments,grades):
    a = int(a.replace(" ",""))
    g = int(g.replace(" ",""))
    p = g + (a*2)
    print(message.format(n,a,g,p))

'''
    Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
    Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.
'''