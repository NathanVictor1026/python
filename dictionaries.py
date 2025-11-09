# all to know about dictionaries
# key value relationship

# an empty dictionary
person = {}

# basic creation
student1 = {"name": "Joan", "age": 21}
 # another way is to use the dict() constructor
student2 = dict(name = "remmy", age = 24)

# how to access values
print(student1["name"])   #OR

print(student2.get("name"))

# wat if i want to add to the dictionaries
student1["gender"] = "female"
student2["gender"] = "male"

#looping through a dictionary
for key, value in student1.items():
    print(key, "->", value)
