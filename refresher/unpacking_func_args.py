def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiply(1,3,5))

def add(a, b):
    return a + b

nums = [3,5]
print(add(*nums))

num_dict = {'a': 3, 'b': 5}
print(add(**num_dict))

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,3,6,7, operator="+"))

print(apply(1,3,6,7, operator="*"))