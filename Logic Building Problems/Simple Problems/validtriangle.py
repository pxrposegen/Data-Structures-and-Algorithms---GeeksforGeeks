def main():
    valueOrder = list()

    print("Enter the Sides of Triangle")
    for i in range(3):
        pointValue = int(input())
        valueOrder.append(pointValue)

    print(f"Validity = {validTriangle(*valueOrder)}")


def validTriangle(a, b, c):
    return False if (a + b <= c) or (a + c <= b) or (b + c <= a) else True


if __name__ == "__main__":
    main()
