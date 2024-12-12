from animal import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis

    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna} dan jenis hewan ini hidup di {self.jenis}')

ikan1 = ikan('ikan Mass', 'pelet', 'tambak', 'bertelur', 'merah', 'air tawar')
ikan1.cetak_ikan()

ikan2 = ikan('Lumba - lumba', 'ikan kecil', 'laut', 'melahirkan', 'abu-abu', 'laut')
ikan2.cetak_ikan()