numbers = [1, 3, 5]
doubled = []

for number in numbers:
    doubled.append(number * 2)

doubled_2 = [number * 2 for number in numbers]

print(doubled)
print(doubled_2)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

starts_s_2 = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
print(starts_s_2)

print("Friends: ", id(friends), "starts_s: ", id(starts_s))