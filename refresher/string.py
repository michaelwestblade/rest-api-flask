name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"

print(f"Hello, {name}")

better_greeting = "Hello, {}"

with_name = better_greeting.format(name)

print(with_name)