list = ["Bob", "Rolf", "Anne"]
tuple = ("Bob", "Rolf", "Anne")
set = {"Bob", "Rolf", "Anne"}

print(list[0])
print(tuple[0])

print(list)
list.append("Smith")
print(list)

set.add("Smith")
print(set)
set.add("Smith")
print(set)

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) # comment

print(local_friends)

print(local_friends.union(abroad))