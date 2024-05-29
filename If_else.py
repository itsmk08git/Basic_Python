n= input("Enter a Number: ")
print(type(n))
n=int(n)
if n%2==0:
    print(f"Number is Even.")
else:
    print(f"Numebr is Odd.")

#Same Program but using Ternary Operator
print("\nUsing Ternary Operator:")
message="Number is Even" if n%2==0 else"Number is Odd"
print(message)
