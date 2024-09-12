def triangle(number):
    for element in range(1,number+1):
        for index in range(1,element+1):
            print(index,end=",")
        print()
triangle(10)



