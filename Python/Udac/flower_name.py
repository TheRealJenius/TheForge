# Write your code here

def flower():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    flowername = {}
    with open("flowers.txt") as f: # need to insert path name for the flowers file
        for line in f:
            flowername[line[0]] = line[3:]
    return flowername[first[0]]
# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name
         
# print the desired output
print(flower())


###Their solution:
'''
# function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()
'''