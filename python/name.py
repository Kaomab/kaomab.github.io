# input methode
#name = input("Name: ")
#print(f"Hello, {name}")

# condution
#n = int(input("Number: "))

# if n > 0:
#    print("n is positive")
# elif n < 0:
#print("n is not positive")
# else:
#    print("n is zero")

# sequences
#name = "kaoma"
# print("name[0]")

# Data structure
# list- sequences of mutable values
# tuple- sequences of immutable values
# set - collection of unique values.
# dict-collection of key-value pair

# define a list of  names
#names = ["kaoma", "kiese", "bienvenue", "nadia"]
# print(names[0])

# names.append("njulu")

# names.sort()

# print(names)


# sets

# empty set
s = set()

# add some element to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s)

s.remove(2)
print(s)
print(f"this set has{len(s)} element")


#loops in python

for i in [0, 1, 2, 3, 4, 5]:
    print(i)
    # or for i rang(6):
    # print(i)
name = "kaoma"
for character in name:
    print(character)
