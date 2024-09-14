import random

firstNumber = random.randint(10, 20)
secondNumber = random.randint(1, 9)
result = firstNumber - secondNumber
userInput = int(input(f" {firstNumber} - {secondNumber} : "))
if userInput == result:
    print("Correct")
else:
    print("Incorrect")

count = 1

while userInput != result:
    count += 1
    userInput = int(input(f" {firstNumber} - {secondNumber} : "))
    if userInput == result:
        print("Correct")
        print( f"number of incorrect answer  : {count - 1}")
        break
    elif count == 10:
        print(count-1)
        break
    else:
        print("Incorrect")