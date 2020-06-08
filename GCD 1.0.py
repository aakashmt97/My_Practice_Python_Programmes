def gcd(m, n):

    factor_m = []
    for x in range(1, m+1):
        if (m % x) == 0:
            factor_m.append(x)

    factor_n = []
    for y in range(1, n+1):
        if (n % y) == 0:
            factor_n.append(y)

    high_num = 0
    low_num_list = []
    if m > n:
        high_num = m
        low_num_list = factor_n
    else:
        high_num = n
        low_num_list = factor_m

    common_factor = []
    for z in range(len(low_num_list)):
        if (high_num % low_num_list[z]) == 0:
            common_factor.append(low_num_list[z])

    return max(common_factor)

print("A programme to find Greatest Common Divisor(GCD)/Common Factor")
m = int(input("Enter the First number: "))
n = int(input("Enter the Second number: "))
result = gcd(m, n)
print("The GDC of your given numbers is :", result)
        
