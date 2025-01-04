def main(): 
    try: 
        userInputA = int(input("Input a = "))
        userInputB = int(input("Input b = "))
        print(f"Before Swap, A = {userInputA} B = {userInputB}")
        userInputA, userInputB = userInputB, userInputA
        print(f"After Swap, A = {userInputA} B = {userInputB}")

    except ValueError:
        print("Invalid Input")

if __name__ == "__main__":
    main()