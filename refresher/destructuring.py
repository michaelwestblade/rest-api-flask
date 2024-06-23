x = (5, 11)

y = 6, 3

z = [(2,3)]

a, b = x

print(a)
print(b)

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(list(friend_ages.items()))

for key, value in friend_ages.items():
    print(key, value)

people = [{"Bob", 42, "Mechanic"}, {"James", 24, "Artist"}, {"Harry", 32, "Professor"}]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

name, _, profession = people[0]

print(f"Name: {name}, Profession: {profession}")

head, *tail = [1,2,3,4,5,6]
*head2, tail2 = [1,2,3,4,5,6]

print(head)
print(tail)
print(head2)
print(tail2)