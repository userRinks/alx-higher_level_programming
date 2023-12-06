#!/usr/bin/python3
"""
Reads input lines from stdin, computes metrics, and prints stats
"""


if __name__ == "__main__":
    import sys

    # Total file size accumulator
    total_file_size = 0

    # Counts of each HTTP status code
    status_code_counts = {}

    while True:
        try:
            # Line processing counter
            counter = 0
            for line in sys.stdin:
                # Split the line into tokens
                line_tokens = line.split()

                # Update total file size
                total_file_size += int(line_tokens[8])

                # Update status code counts
                status_code = line_tokens[7]
                if status_code not in status_code_counts:
                    status_code_counts[status_code] = 1
                else:
                    status_code_counts[status_code] += 1

                # Break after processing 10 lines
                if counter == 10:
                    break
                counter += 1

        # Exit gracefully on keyboard interrupt
        except KeyboardInterrupt:
            exit()
        finally:
            # Print computed metrics
            print("File size: {}".format(total_file_size))
            for key in sorted(status_code_counts):
                print("{}: {}".format(key, status_code_counts[key]))
