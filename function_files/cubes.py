def that_Number_Can_Multiply_Itself_Three_Times(param):
    cube_number = {}
    for number in param:
        cube_number[number] = number **3
        print(cube_number)
    return cube_number