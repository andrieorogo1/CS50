people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}    
] 

def f(person):
    return person["house"]

# people.sort(key=f)
people.sort(key=lambda person: person["name"])
print(people)

"""
Traceback (most recent call last):
  File "/Users/andrie/Documents/cs50/python/lambda.py", line 7, in <module>
    people.sort()
TypeError: '<' not supported between instances of 'dict' and 'dict'

Thoughts: The sort function cannot compare the two dictionary, it should have a function 
to read the list of dictionary to know what to sort.

"""

