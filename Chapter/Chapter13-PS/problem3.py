arr  = [1, 20, 34234, 53, 6234235, 64343, 65, 754, 45, 55]


def divisible5(n):
    if(n % 5 == 0):
        return True
    
    return False

res = list(filter(divisible5, arr))

print(res)