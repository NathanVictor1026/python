# what i need to know about strings
# sequence of characters letters, numbers, spaces, in quotes
firstName = "Nathan"
lastName = "Kyeyune"

# Concatenation - joining two or more strings
fullName = firstName + lastName

# slicing - extracting parts of a string
print(fullName[0:5])

# indexing - characters
print(lastName[4])

# length of strings
print(len(fullName))

# OTHER STRING METHODS 
wrongName = "Mecky"
# Replace wrong letter
print(wrongName.replace("M", "B"))

girl = "winnie"
print(girl.title())

# f-strings - strings with texts and variables
student = "Mark"
gender = "male"
print(f"My name is {student} and I am a {gender}.")
