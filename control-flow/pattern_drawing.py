pattern = int(input("Enter the size of the pattern: "))
rows = pattern
while (rows>0):
    for i in range(0, pattern):
        print("*", end=" ")
    print()
    rows -= 1