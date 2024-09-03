#!/usr/bin/python3
"""Algoritm to determine the winner of the primegame for given rounds
and chosen nums"""

def isWinner(x, nums):
    """returns the winner the winner"""
    def sieve_of_eratosthenes(n):
        """marks primes as true"""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        return primes

    def determine_winner(n):
        """ determine the winner for a round"""
        primes = sieve_of_eratosthenes(n)
        prime_count = sum(primes)
        return "Maria" if prime_count % 2 == 1 else "Ben"

    if not nums or x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
print("Winner: {}".format(isWinner(1, [1])))
