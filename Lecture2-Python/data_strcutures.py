# list
print("***** list *****")
names = ["Jesus", "Joshua", "Mary"]
print(names)

names.append("Adam")
names.sort()
print(names)

# tuple
print("***** tuple *****")

# set
print("***** set *****")
s = set()
print(s)

s.add(1)
s.add(9)
s.add(0)
s.add(3)
print(f"New values added: {s}")

s.remove(0)
print(f"One value removed: {s}")

# dictionary
print("***** dict *****")
cities = {"Los Angeles": "California", "New York City":"New York"}
print(cities)
print(cities["Los Angeles"])
cities["Los Angeles"] = "CA"
print(cities["Los Angeles"])