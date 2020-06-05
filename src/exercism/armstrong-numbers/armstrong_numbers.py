def is_armstrong_number(number):
    exp = len(str(number))
    sum = 0
    for n in str(number)[0:exp:1]:
        sum += int(n)**exp 
    return sum == number
