def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    return a * pangkat_rekursif(a, b - 1)   # a = angka biasa , b = pangkat

print(pangkat_rekursif(2, 5))