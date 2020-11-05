def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# A simple method to evaluate
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
 
# Driver Code
x = int(input("Enter number: "))
for n in range(1, x+1):
    print("phi(",n,") = ", 
           phi(n), sep = "")
            