def triangle(number):
    for row in range(1,number+1):
        for colum in range(1,number+2 -row):
            print(colum,end=" ")

        print()
triangle(10)