def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.strip().split(",")[0]) # stip the line from the list, then split it into seperate portions, then indext to the 0 variable
            '''thier answer:
            name = line.split(",")[0]
            cast_list.append(name)
            '''
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt') #need to input the rest of the path to get it to work outside of class
for actor in cast_list:
    print(actor)