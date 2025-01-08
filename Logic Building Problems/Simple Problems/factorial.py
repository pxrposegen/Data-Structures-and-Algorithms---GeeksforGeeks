def main(): 
    userInput = int(input("Input: "))
    prod = 1

    for i in range(2,userInput+1):
        prod *= i

    print(f"Factorial of {userInput} = {prod}")

main()