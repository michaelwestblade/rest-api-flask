def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

details = {"name": "Bob", "age": 25}

named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(**details)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)