"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkIfPrime(num):
    for i in range(2, (num // 2)+1):
        if num%i == 0:
            return 0
    else:
        return 1
    
    
def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    
    list = [2]
    start = 3

    while len(list) <= number_of_primes - 1:
        isPrime = checkIfPrime(start)
        if isPrime:
            list.append(start)

        start += 1

    return list
    


