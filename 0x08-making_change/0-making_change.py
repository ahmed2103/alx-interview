#!/usr/bin/python3
"""Minimum unique way to make change module"""


def makeChange(coins, total):
    """Minimum ways to make coin change module buttom up approach"""
    if total <= 0:
        return 0
    memo = dict()

    def dp(amount):
        """helper function"""
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        min_coins = float('inf')
        for coin in coins:
            if coin <= amount:
                min_coins = min(min_coins, dp(amount - coin) + 1)

        memo[amount] = min_coins
        return min_coins

    result = dp(total)
    return result if result != float('inf') else - 1
