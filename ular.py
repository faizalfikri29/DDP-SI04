from animal import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis

    def cetak_ular(self):
        super().cetak()
        print(f'Warna hewan ini {self.warna} dan hewan ini {self.jenis}')

ular1 = ular('Piton', 'daging', 'darat', 'bertelur', 'coklat', 'tidak berbisa')
ular1.cetak_ular()

ular2 = ular('cobra', 'daging', 'darat', 'bertelur', 'Hitam ke abu - abu an', 'berbisa')
ular2.cetak_ular()