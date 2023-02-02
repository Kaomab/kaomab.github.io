
people = [
    {"name": "kaoma", "house": "Gryffindor"},
    {"name": "cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]


def f(person):
    return person["house"]


people.sort(key=lambda person: person["Name"])
# this is aqual

# people.sort(key=f)
print(people)
