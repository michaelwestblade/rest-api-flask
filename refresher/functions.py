friends = ["Rolf", "Bob"]

# def add_friend():
#     friend_name = input("Enter a name: ")
#     f = friends + [friend_name]
#
# add_friend()

def add(x, y):
    result = x + y
    return result

print(add(2, 3))


def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Westblade", name="Michael")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Dividend is zero")

divide(5, 0)
divide(dividend=15, divisor=5)

def default_add(x, y=8):
    result = x + y
    return result

print(default_add(5))