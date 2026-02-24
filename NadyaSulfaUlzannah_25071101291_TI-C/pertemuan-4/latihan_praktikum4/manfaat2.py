# program merespons kesalahan
try:
    umur = int(input("Masukkan umur: "))
except ValueError:
    print("Input harus berupa angka!")

# Program menjadi lebih aman dan tidak mudah rusak.