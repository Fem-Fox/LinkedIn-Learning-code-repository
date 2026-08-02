def factorial(num):
    if type(num) == int:
        if num > 0:
            num_2 = 1
            result = num
            while num - num_2 >= 1:
                result *= (num - num_2)
                num_2 += 1
            return result
        elif num == 0:
            num_zero = 1
            return num_zero
        else:
            return None
    else:
        return None
    
print(factorial(4))
print(factorial(0))
print(factorial(-3))
print(factorial("Spam"))


