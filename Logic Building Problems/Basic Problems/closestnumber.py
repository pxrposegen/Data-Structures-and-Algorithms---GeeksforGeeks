"""
Find the number closest to n which is divisible by m
"""

def main(): 
    userInputA = int(input("Enter the number: "))
    userInputB = int(input("Enter the number to check divisibility with: "))
    print(f"Output: {closestnumber(userInputA,userInputB)}")

def closestnumber(n,m): 
    q = int(n/m) 

    c1 = q*m # First Closest Number

    if n*m < 0: 
        c2 = (q-1) * m # Second Closest Number if any one of the number is negative
    else: 
        c2 = (q+1) * m  # Second closest number if both numbers are positive

    return c1 if abs(n - c2) < c1 else c2 

main()

    