def multiply(a, b=None):
    if b is None:
        return a * a
    return a * b

print(multiply(3))
print(multiply(3,4))
