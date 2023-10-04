"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("The list must be of a length above 0.")

    list = []
    index = 2
    while number_of_primes > 0:
        if checkPrime(index):
            list.append(index)
            number_of_primes -= 1
        index += 1
    return list

def checkPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

