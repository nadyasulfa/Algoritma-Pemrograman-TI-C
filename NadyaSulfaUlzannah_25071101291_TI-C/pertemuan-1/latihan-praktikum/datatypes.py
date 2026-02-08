# Data type (tipe data) adalah jenis data yang disimpan dalam variabel
# 1. Setting the Data Type, code otomatis menentukan tipe data berdasarkan nilai yang diberikan
umur = 19     # int
tinggi_badan = 157.5  # float
nama = "Nadya"  # str
status = True   # bool 

# 2. Built-in Data Types, tipe data bawaan : int, float, str, bool, lost, tuple, dict
buah = ["apel", "jeruk"]      # list
banyak_buah = (5, 3)            # tuple
rasa_buah = {"manis": "asam"}    # dict

# 3. Getting the Data Type, Untuk mengetahui tipe data suatu variabel, gunakan fungsi type()
print(type(umur))
print(type(tinggi_badan))
print(type(nama))
print(type(status))
print(type(buah))
print(type(banyak_buah))
print(type(rasa_buah))

# 4. Setting the Specific Data Type, menentukan tipe data secara spesifik menggunakan fungsi bawaan (casting) 
x = int(5.7)
y = float(10)
z = str(123)
b = bool(1)

print(x)
print(y)
print(z)
print(b)
