def main(): 
    print("Enter the values")
    print("Press Q to Exit")

    userInput = list()

    while True: 
        choice = input()
        if choice.upper() != "Q":
            userInput.append(int(choice))
        else:
            break
    
    userInput.sort()
    print(f"Arithmetic Progression Check: {checkap(userInput)}")

           
def checkap(n): 
    if len(n) <= 0: 
        return False
    
    if len(n) == 1: 
        return True
    else: 
        d = n[1] - n[0]
        for i in range(2,len(n)-1):
            if n[i+1] - n[i] != d: 
                return False
        return True

if __name__ == "__main__":
    main()