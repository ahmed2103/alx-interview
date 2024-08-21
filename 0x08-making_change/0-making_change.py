#!/usr/bin/python3
"""Minimum unique way to make change module"""


def makeChange(coins, total):
    """Minimum ways to make coin change module buttom up approach"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
