def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        total += float(n)
    return total / len(values)

print("Welcome, utils module has been imported and initialised!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print("Average is", average(sys.argv[1:]))
    else:
        print("No arguments provided")
