def bil_prima(n):
    prima = []
    for angka in range(2, n + 1):  # dimulai dari 2 krn bil.prima di mulai dari angka 2
        angka_prima = True
        for i in range(2, angka):
            if angka % i == 0:
                angka_prima = False
                break
        if angka_prima:
            prima.append(angka)
    return prima

hasil_prima = bil_prima(50)
print(hasil_prima)