from animal import *

class ayam(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
        self.jenis = jenis

    def cetak_ayam(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna_bulu} dan jenis hewan ini adalah {self.jenis}')

kapas = ayam('ayam kapas', 'puur', 'darat', 'bertelur', 'putih gembul', 'betina')
kapas.cetak_ayam()

cemani = ayam('ayam Cemani', 'puur', 'darat', 'bertelur', 'hitam', 'jantan')
cemani.cetak_ayam()