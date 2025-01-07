from math import sqrt

def main(): 
    valueOrder = list()
    
    for i in range(4): 
        pointValue = int(input("Enter the points x1,y1,x2,y2 in Order: "))
        valueOrder.append(pointValue)
    
    print(f"Distance = {distanceCalculator(*valueOrder):.2f}")

def distanceCalculator(x1,y1,x2,y2):
    return(sqrt(pow(x2-x1,2) + pow(y2-y1,2)))

if __name__ == "__main__": 
    main()