num = input(input("Enter a five digits number : "))

digit1 = num % 10
num //= 10
digit2 = num % 10
num //= 10
digit3 = num % 10
num //= 10
digit4 = num % 10
num //= 10
digit5 = num % 10

print(digit1 , end="  ")
print(digit2 , end="  ")
print(digit3 , end="  ")
print(digit4 , end="  ")
print(digit5)