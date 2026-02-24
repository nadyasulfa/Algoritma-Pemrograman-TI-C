""" input() adalah fungsi yang selalu 
    mengembalikan data sebagai string """

nama = input("Masukkan nama : ")
print("Hallo", nama)
print(type(nama))


""" jika ingin melakukan operasi perhitungan 
    maka perlu dilakukan konversi tipe data """

angka = int(input("Masukkan angka : "))
print(angka + 5)


""" jika tidak melakukan konversi tipe data 
    saat melakukan operasi perhitungan
    maka yang terjadi adalah  Typeerror """

bilangan = input("Masukkan bilangan bulat : ")
hasil = bilangan + 5

