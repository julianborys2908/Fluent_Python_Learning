import array

symbols = "$¢£¥€¤"

created_tuple = tuple(ord(symbol) for symbol in symbols)

print(created_tuple)

created_array = array.array("I", (ord(symbol) for symbol in symbols))

print(created_array)

colors = ["white", "black"]
sizes = ["S", "M", "L"]

for tshirt in (f"{color} {size}" for color in colors for size in sizes):
    print(tshirt)
