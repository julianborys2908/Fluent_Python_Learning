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
