import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   
    #math.sqrt digunakan untuk menghitung akar kuadrat yang ada di rumus

hasil_jarak = jarak(1, 2, 3, 4)
print(f"Jarak = {hasil_jarak:.2f}")  # .2f = hanya menuliskan 2 angka di belakang koma
