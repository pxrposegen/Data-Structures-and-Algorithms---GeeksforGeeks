def is_perfect_number(n):
    if n <= 1:
        return False  # Perfect numbers must be greater than 1
    
    divisor_sum = 1  

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  
                divisor_sum += n // i
    
    return divisor_sum == n

if __name__ == "__main__":
    test_numbers = [6, 28, 496, 12, 8128, 33550336, 9]
    for num in test_numbers:
        result = is_perfect_number(num)
        print(f"{num} is a perfect number: {result}")
