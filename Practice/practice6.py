a = int(input("a:"))
b = int(input("b:"))
operator = int(input("Enter operation (1 for +, 2 for -, 3 for *):"))
if operator == 1:
    print("a + b =", a + b)
elif operator == 2:
    print(a - b)
elif operator == 3:
    print("a * b =")
else:
    print("Invalid operation")