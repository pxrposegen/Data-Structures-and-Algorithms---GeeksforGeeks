from math import sqrt

def main(): 
    try: 
        userInput = int(input("Input: "))
        if userInput < 2: 
            print("No Prime")
        else: 
            print(f"Prime = {bool(checkPrime(userInput))}")
    except ValueError: 
        print("Invalid Input!")

def checkPrime(n): 
    for i in range(2,int(sqrt(n)) + 1):
        if n%i == 0: 
            return 0
    return 1

if __name__ == "__main__":
    main()