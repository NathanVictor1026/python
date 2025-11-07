# everything about lists
# ordered and changable collection
classmates = []

# adding members to the list
classmates.append("Nate")
classmates.append("Mark")
classmates.append("Steve")
classmates.append("Frank")
classmates.append("Jeff")
classmates.append("Imma")

#removing items from a list
#you can remove by value, or by index
classmates.remove("Imma")
print(classmates)

# printing each member. use a loop
for mate in classmates:
    print(mate)
