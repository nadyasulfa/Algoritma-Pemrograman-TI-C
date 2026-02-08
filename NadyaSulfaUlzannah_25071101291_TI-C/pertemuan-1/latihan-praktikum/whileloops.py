# PYTHON WHILE LOOPS

# 1. Python Loops & while Loop
# while, perulangan selama kondisi bernilai True, jika nilai Fale, perulangan berhenti

angka = 1

while angka <= 5:
    print("Angka:", angka)
    angka += 1


# 2. break Statement
# Menghentikan loop secara paksa, walau kondisi masih True

angka = 1

while angka <= 10:
    print("Angka:", angka)

    if angka == 5:
        print("Loop dihentikan dengan break")
        break

    angka += 1


# 3. continue Statement
# Melewati satu perulangan dan lanjut ke perulangan berikutnya

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        print("Angka 3 dilewati")
        continue

    print("Angka:", angka)


# 4. else Statement pada while
# else dijalankan jika loop selesai secara bormal (tanpa break)

angka = 1

while angka <= 3:
    print("Perulangan ke:", angka)
    angka += 1
else:
    print("Loop selesai secara normal")
