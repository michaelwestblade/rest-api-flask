add = lambda x, y: x + y

print(add(1, 2))

def double(x):
    return x * 2

sequence = [1,3,5,9]
doubled = [double(x) for x in sequence]
print(sequence)
print(doubled)

doubled = map(double, sequence)
print(list(doubled))