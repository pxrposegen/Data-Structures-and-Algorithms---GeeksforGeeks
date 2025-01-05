"""
Calculating the the Area of a Circle using Math Module
"""

from math import pi 

def main(): 
    userInput = float(input("Enter the Radius: "))

    print(f"Area = {pi*(userInput**2)}")

if __name__ == "__main__": 
    main()