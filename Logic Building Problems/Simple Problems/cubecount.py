"""
Given n, count all 'a' and 'b' that satisfy the condition a^3 + b^3 = n, 
where (a,b) and (b,a) are considered two different pairs
"""

import math 

def main(): 
    userInputN = int(input("Input: "))
    print(f"Total Pairs = {pairs(userInputN)}")

def pairs(n): 
    """
    Logic
    Iterate upto cube root of n, since a^3 = n - b^3 iff a <= cube root of n 
    Find aCube 
    bCube = n - aCube 
    b = round(bCube ** 1/3)

    check whether b is a perfect cube, if yes -> increment count
    """

    count = 0
    for i in range(1,math.pow(n,1/3)+1):
        aCube = i**3 
        b = n - aCube

        bCube = round(b ** 1/3)

        if bCube**3 == b:
            count+=1

    return count

if __name__ == "__main__":
    main()