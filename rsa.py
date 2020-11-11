from decimal import Decimal

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def calct(no,e, n):
    ctt = Decimal(0)
    ctt = pow(no, e)
    ct = ctt % n
    return ct

def caldt(ct, d, n):
    dtt = Decimal(0)
    dtt = pow(ct, d)
    dt = dtt % n
    return dt

def s1():
    p = int(input('Enter the value of p = ')) 
    q = int(input('Enter the value of q = ')) 
    no = int(input('Enter the message M = ')) 
    e = int(input('Enter the value of e = '))
    
    n = p*q
    t = (p-1)*(q-1)

    d = 0
    for i in range(1,10):
        x = 1 + i*t
        if x & e == 0:
            d = int(x/e)
            break
    ct = calct(no, e, n) 
    dt = caldt(ct, e, n) 

    print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 

def s2():
    p = int(input('Enter the value of p = ')) 
    q = int(input('Enter the value of q = ')) 
    no = int(input('Enter the message M = ')) 
    d = int(input('Enter the value of d = '))
    
    n = p*q
    t = (p-1)*(q-1)

    for e in range(2,t): 
        if gcd(e,t)== 1: 
            break
    ct = calct(no, e, n)
    dt = caldt(ct, d, n)
    print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))

def main():
    inp = input('0 for p q M e | 1 for p q M d: ')
    if inp == 0:
        s1()
    else: 
        s2()

main()