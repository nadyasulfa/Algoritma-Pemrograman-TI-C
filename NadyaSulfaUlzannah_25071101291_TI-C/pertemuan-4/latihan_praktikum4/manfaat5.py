# dapat mengetahui jenis error yang terjadi tanpa dituliskan dalam code
try:
    x = 10 / 0
except Exception as i:
    print("Terjadi error:", i)