a =  float(input("Enter Number a: "))
b =  float(input("Enter Number b: "))
op =  input("Enter Number operator (+, -, *, /, %, **): ")


if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a %b)
elif op == "**":
    print(a**b)
else: 
    print("Invalid")