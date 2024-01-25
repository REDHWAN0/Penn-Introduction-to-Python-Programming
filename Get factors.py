def get_factors (x):
    """returns a list of factors of given number x"""
    factors = []
    #iterate over range from 1 to number x
    for i in range (1, x + 1):
        
        #check if i divide number x evently
        if (x % i == 0):
            factors.append(i)
    return factors
print(get_factors(17))