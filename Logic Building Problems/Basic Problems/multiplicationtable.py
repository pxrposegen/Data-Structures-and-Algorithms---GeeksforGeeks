def main(): 
    try: 
        userInput = int(input("Input: "))
        for i in range(1,11): 
            print("%d * %d = %d" % (userInput,i,userInput*i))
    except: 
        print("Invalid Input")

if __name__ == "__main__":
    main()