"""
Sum of N natural numbers = n * (n +1) / 2
"""

def main(): 
    userInput = int(input("Input: "))
    print(f"Output: {int(userInput * (userInput + 1) / 2)}")

if __name__ == "__main__": 
    main()