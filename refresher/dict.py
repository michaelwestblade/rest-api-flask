friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20

print(friend_ages)

friends = [{"name": "Rolf", "age": 24}, {"name": "Adam", "age": 30}, {"name": "Anne", "age": 27}]

print(friends[0]["age"])

if "Adam" in friends:
    print(friends["Adam"]["age"])

ages = friend_ages.values()
print(sum(ages) / len(friends))