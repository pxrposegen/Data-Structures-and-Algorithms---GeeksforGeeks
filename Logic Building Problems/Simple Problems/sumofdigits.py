"""
A program which calculates the sum of digits of a number
"""

def main(): 
    userInput = int(input("Input: "))
    print(f"Sum of Digit = {digitSum(userInput)}")

def digitSum(n): 
    sum = 0

    while n > 0:
        r = n % 10
        sum += r
        n //= 10

    return sum


if __name__ == "__main__":
    main()