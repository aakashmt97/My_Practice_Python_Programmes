def gcd(m, n):
    
    low_num = min(m, n)

    common_factor = 0
    for i in range(1, (low_num + 1)):
        if (m % i) == 0 and (n % i) == 0:
            common_factor = i

    return common_factor
print("Program to find Greatest Common Divisor (GCD)")
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
result = gcd(m, n)
print("The GCD of your given numbers is ", result)
        
