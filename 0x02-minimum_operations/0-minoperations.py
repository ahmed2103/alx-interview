#!/usr/bin/python3
"""Module to find the minimum number of operations required
   to solve interview problem."""


def minOperations(n):
    """Function to find the minimum number of operations required"""
    if n == 0:
        return 0
    denominator = 2
    primes = []
    while n > 1:
        while n % denominator == 0:
            primes.append(denominator)
            n //= denominator
        if n == 1:
            break
        denominator += 1
        if denominator**2 > n:
            primes.append(n)
            break
    return sum(primes)
