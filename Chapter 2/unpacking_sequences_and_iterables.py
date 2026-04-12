print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)


a, b, *rest = range(5)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)


def function(a, b, c, d, *rest):
    return f"a: {a}, b: {b}, c: {c}, d: {d}, rest: {rest}"


print(function(*[1, 2], 3, *range(4, 7)))

metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")


main()
