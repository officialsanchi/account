

def odd_index(number):
    for element in range(1,number+1):
        for index in range(1, element+1):
            if index %2 == 1:
                print(index,end=" ")
            else:
                print("-",end=" ")

        print()

odd_index(10)