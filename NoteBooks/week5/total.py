import sys

count = len(sys.argv)

if count <= 1:
    print("No arguments were provided")
else:
    total = 0
    c = count

    while c > 1:
        c -= 1
        total += float(sys.argv[c])

    average = total / (count - 1)

    print("Total is", total)
    print("Average is", average)
