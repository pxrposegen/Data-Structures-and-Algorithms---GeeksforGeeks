def main(): 
    try:
        userInput = int(input("Input n = "))
        print(f"Output: {sum(userInput)}")
    except: 
        print("Invalid Input")

def sum(n):
    sum = 0 
    for i in range(1,n+1):
        sum += i
    return sum 


if __name__ == "__main__": 
    main()