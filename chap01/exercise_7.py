print("This Program ilustrates a chaotic function")
n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a value between 0 and 1: "))
y = eval(input("Enter a different value between 0 and 1: "))
for i in range(n):
    x = 3.9 * x - 3.9 * x * x
    y = 3.9 * y - 3.9 * y * y 
    print(x, y)
