#lists - with []- store many pieces of connected / related data in order
#counting starts from 0 - how many places position is shifted from beginning of the list
states_of_america = ["Delaware", "Pensylvania", "...etc.."]

print(states_of_america[0])

print(states_of_america[2])
# counting down from the end starts from-1 - not from-0 ;)
print(states_of_america[-1])

#changing value of particular item in list - chane "Pensylvania" to "orange_cat":
states_of_america[1] = "orange_cat"

print(states_of_america)

#add an item to end of list with one lement
states_of_america.append("Mechatek")

print(states_of_america)
# add many items into list
states_of_america.extend(["ściera", "Kika"])

print(states_of_america)