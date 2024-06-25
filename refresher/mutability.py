a = []
b = a

print("aid", id(a))
print("bid", id(b))

a.append(35)

print("aid", id(a))
print("bid", id(b))

print("a", a)
print("b", b)