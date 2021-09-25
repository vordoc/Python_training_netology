def square(number):
    '''
    this is my function
    '''
    result = number**2
    return result
res = square(3)
print(res)

help(square)

def s_square():
    user_number = int(input("Enter a number"))
    result_1 = user_number ** 2
    return result_1
res_1 = s_square()
print(res_1)