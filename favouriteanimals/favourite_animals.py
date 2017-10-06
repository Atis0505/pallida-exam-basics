# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys

animals_from_user = sys.argv

def check_user_inputs(user_inputs):
    if len(user_inputs) == 1:
        print("fav_animals [animal] [animal]")
    elif len(user_inputs) == 2:
        print("Give your favourite animal!")
    else:
        list_of_animals = []
        for i in range(2,len(user_inputs)):
            list_of_animals.append(user_inputs[i])
        save_animals(list_of_animals)


def save_animals(animals_list):
    for animal in animals_list:
        with open("favourites.txt", "r+") as f:
            for line in f:
                if animal in line:
                    break
            else:
                f.writelines(animal + "\n")
        
    
check_user_inputs(animals_from_user)