
def get_factorial(num):
    result = 1
    for num in range(1, num + 1):
        result *= num
    return result

def sum_odd_numbers(num):
    result = 0
    x = 1
    while x <= num:
        if x % 2 != 0:
            result += x
        x += 1
    return result
