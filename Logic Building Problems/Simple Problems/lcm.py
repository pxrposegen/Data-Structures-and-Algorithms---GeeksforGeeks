from gcd import gcd 

def lcm(a,b): 
    return int((a*b)/gcd(a,b))

def main(): 
    userInputA = int(input("Input a: "))
    userInputB = int(input("Input b: "))

    print(f"LCM = {lcm(userInputA,userInputB)}")

if __name__ == "__main__":
    main()
