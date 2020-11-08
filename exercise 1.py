def compare(x,y):
    if x > y:
        print(1)
    elif x < y:
        print(-1)
    elif x == y:
        print(0)

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))
compare(x, y)
