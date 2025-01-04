def main(): 
    userInput = int(input("Enter the Dice Face: "))
    oppositeFace = 7 - userInput
    print(f"Output: {oppositeFace}")

if __name__ == "__main__":
    main()