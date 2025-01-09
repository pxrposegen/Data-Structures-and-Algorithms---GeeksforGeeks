"""
GCD of 2 numbers
"""


def gcd(a, b):
    i = min(a, b)

    while i:
        if a % i == 0 and b % i == 0:

            break

        i -= 1

    return i


def main():
    print(f"GCD of 98 and 56 = {gcd(98,56)}")


main()
