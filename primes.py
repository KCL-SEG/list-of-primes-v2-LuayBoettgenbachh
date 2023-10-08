"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkIfPrime(num):
    for i in range(2, (num // 2)+1):
        if num%i == 0:
            return 0
    else:
        return 1
    


