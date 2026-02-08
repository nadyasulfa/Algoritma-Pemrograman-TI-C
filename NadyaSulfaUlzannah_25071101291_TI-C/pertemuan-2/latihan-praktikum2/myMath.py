def penambahan(a,b):
    return a + b 
print(penambahan (6,8))

def pengurangan(a,b):
    return a - b 
print(pengurangan(5,3))

def perkalian(a,b):
    return a * b 
print(perkalian(5,5))

def pembagian(a,b):
    return a / b 
print(pembagian(6,3))

def modulus(a,b):
    return a % b 
print(modulus(4,3))

n = 5
def fibonancci(n):
    if n <= 1:
        return n
    else:
        return fibonancci(n - 1) + fibonancci(n - 2)

for i in range(n):
    print(fibonancci(n-i))