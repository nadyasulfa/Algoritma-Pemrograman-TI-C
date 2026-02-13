class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    def sound(self):
        print("suara")
    
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
        super().__init__(jenis, merk, tahun_rilis)
        self.__suara = "ngeng ngeng"

    def get_suara(self):
        return self.__suara

class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
        super().__init__(jenis, merk, tahun_rilis)
        self.__suara = "brum brum"

    def get_suara(self):
        return self.__suara

kdr = Vehicle("metik", "beat", 2020)
mtr = Motor("manual", "revo", 2019)
mbl = Mobil("metik", "pajero", 2021)

print(kdr.merk)
print(mtr.get_suara())
print(mbl.get_suara())
