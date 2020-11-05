x = int(input("Input your number: "))
e = int(input("Input your power number: "))   
m = int(input("Input your modular number: "))

def squarenmul(num,expo,modu):
    bin2 = bin(expo)[3:]
    length = len(bin2)
    r = num
    for x in range(length):
        r = (r*r) % modu
        if bin2[x] == '1':
            r = (r*num) % modu    
    return r

print(squarenmul(x,e,m))

