def get_factors(number):
    from math import sqrt as sqrt
    # init some vars
    factors = []
    sq_root = sqrt(number)
    i = 1
    # find the factors
    while i <= sq_root:
        if number % i == 0:
            # add factor to the list
            factors.append(int(i))
            # get the associated factor
            i2 = int(number / i)
            if i2 != i and i2 != number:
                # not the sqrt or the number itself
                factors.append(i2)
        i += 1  
    return factors

def classify(number):
    # sanity check
    if number < 1:
        raise ValueError('Number is less than 1')
    # get the total of all the factors
    factor_sum = int(sum(get_factors(number)))
    # do the classification
    if number == 1:
        # 1 is an edge case
        return 'deficient'
    elif factor_sum == number:
        return 'perfect'
    elif factor_sum < number:
        return 'deficient'
    elif  factor_sum > number:
        return 'abundant'
