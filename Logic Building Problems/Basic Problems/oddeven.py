def main(): 
    try:
        user_input = int(input("Input: "))
        print(f"Output: {OddEven(user_input)}")

    except: 
        print("Invalid Input")
        
def OddEven(n):
    return True if n%2 else False

if __name__ == "__main__":
    main()