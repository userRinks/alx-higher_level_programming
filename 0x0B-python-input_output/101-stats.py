#!/usr/bin/python3
"""
101-stats.py - Computes metrics from stdin
"""

import sys

def print_metrics(total_size, status_codes):
    """
    Print metrics based on total file size and status codes.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary with status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """
    Parse a line and update metrics.

    Args:
        line (str): Input line.
        total_size (int): Current total file size.
        status_codes (dict): Dictionary with status codes and their counts.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]

        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        return total_size, status_codes
    except ValueError:
        return total_size, status_codes

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_codes = parse_line(line, total_size, status_codes)

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
