def jumlah_digit(n):                            
    if n == 0:                                  # % 10  = digunakan untuk angka desimal (biasa)
        return 0                                # % 10  = mengambil digit angka terakhir
    return n % 10 + jumlah_digit(n // 10)       # // 10 = membuang digit angka terakhir

print(jumlah_digit(1234))