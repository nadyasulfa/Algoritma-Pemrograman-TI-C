# PYTHON NUMBERS

# 1. Int, bilangan bulat
a = 10

# 2. Float, bilangan desimal
b = 3.5

# 3. Complex, bilangan kompleks (j)
c = 2 + 4j

# 4. Menampilkan nilai dan tipe data
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 5. Type Conversion, mengubah tipe angka
x = float(a)      # int ke float
y = int(b)        # float ke int
z = complex(a)    # int ke complex

print(x, type(x))
print(y, type(y))
print(z, type(z))

# 6. Random Number, menghasilkan angka acak
import random    # memanggil modul random bawaan python
angka_acak = random.randint(1, 10)   # membuat angka acak, randint(1, 10), menghasilkan angka acak

print("Angka acak:", angka_acak)  # menampilkan angka acak, output tidak selalu angka yang sama
