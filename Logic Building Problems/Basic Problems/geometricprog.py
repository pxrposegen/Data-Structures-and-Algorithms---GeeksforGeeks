"""
Program to find the sum of geometric progression series

Sum of n = a * ((1 - r^n)/(1 - r))
"""

def main(): 
    print("Enter the List of Numbers")
    print("Press Q to Exit!")

    userInput = list()
    running =- True

    while running: 
        values = input()
        if values.upper() == "Q":
            running = False
        else: 
            userInput.append(int(values))
    
    if len(userInput) > 0:
        r, flag = checkgeo(userInput)

        if flag == 1 and r != 0: 
            print(f"Geometric Sum = {geometricsum(userInput,r)}")

        else: 
            print("Not a Geometric Progression!")

def checkgeo(n): 
    if len(n) <= 2: 
        return 0,0
        
    else: 
        r = n[1] / n[0]
        for i in range(2,len(n)-1):
            if n[i+1] / n[2] != r: 
                return r,0
        
        return r,1
    
def geometricsum(n,r): 
    return (n[0] * ((1 - r**len(n))/(1 - r)))

if __name__ == "__main__":
    main()