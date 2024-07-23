#!/usr/bin/python3
"""Python function that validates UTF-8 string"""


def validUTF8(data):
    """Validates data set if being in UTF-8 format"""
    n_bytes = 0
    mask1 = 1 << 7  # check the most significant bit
    mask2 = 1 << 6

    for num in data:
        byte = num & 255  # As we want it in bits.
        if n_bytes == 0:
            mask = mask1
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1  # to mask the next bit

            if n_bytes == 0:
                continue   # ASCII

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
