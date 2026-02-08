# Python Booleans
# 1. Boolean Values (nilai ditulis dengan huruf awal besar)
print(True)
print(False)

# 2. Evaluate Values and Variables (evaluasi nilai atau variabel menentukan hasilnya True atau False)
angka = 10
teks = "Python"

print(bool(angka))
print(bool(teks))

# 3. Most Values are True (Hampir semua nilai bernilai True)
print(bool(1))              # Contohnya :
print(bool(5.5))            # Angka selain 0
print(bool("Belajar"))      # Str yang tidak kosong
print(bool([1, 2, 3]))      # List yang berisi data

# 4. Some Values are False (bebrapa nilai akan bernilai False)
print(bool(0))              # 0
print(bool(""))             # "" (str kosong)
print(bool([]))             # [] (list kosong)
print(bool(None))           # none

# 5. Functions can Return a Boolean
# Fungsi bisa mengembalikan nilai bool (True atau False)
def punya_ktp(umur):
    if umur >= 17:
        return True
    else:
        return False

print(punya_ktp(19))
print(punya_ktp(15))
