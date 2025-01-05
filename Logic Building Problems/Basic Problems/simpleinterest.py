"""
Program to calculate Simple Interest using the Formula I = P*R*T/100
"""

def main(): 
    principal = int(input("Enter the Principal Amount: "))
    interestRate = int(input("Enter the Interest Rate Percentage: "))
    timePeriod = int(input("Enter the Time Period: "))

    print(f"Interest = {calculateinterest(principal,interestRate,timePeriod)}")

def calculateinterest(p,r,t = 1): 
    return float((p*r*t)/100)

if __name__ == "__main__": 
    main()