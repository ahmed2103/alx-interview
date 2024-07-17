#!/usr/bin/python3
"""Script to do some statistics calculations and handles exceptions"""

import sys


def print_stats(size, status_codes):
    """Function prints precalculated statistics"""
    print("File size:", size)
    for code in sorted(status_codes.keys()):  # to gurantee order
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function of the script logic"""
    status_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    total_size = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split(" ")
                size = int(parts[-1])
                status = int(parts[-2])

                total_size += size
                if status in status_dict:
                    status_dict[status] = status_dict[status] + 1
            except (IndexError, ValueError):
                pass
            if line_count % 10 == 0:
                print_stats(total_size, status_dict)
    except KeyboardInterrupt:
        print_stats(total_size, status_dict)
        raise

    print_stats(total_size, status_dict)  # if ended normally


if __name__ == '__main__':
    main()
