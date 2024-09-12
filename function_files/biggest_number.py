def biggest_number(numbers):
    maximum = 0
    for index in numbers:
        if int(index) > maximum and int(index) % 2 != 0:
             maximum = int(index)

                return maximum