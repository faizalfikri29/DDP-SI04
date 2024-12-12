class animal:

    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak (self):
        print(f'Hewan {self.nama}, hewan ini memakan {self.makanan} hidupnya di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}')

# he1 = animal('singa', 'daging', 'gurun sahara', 'melahirkan')
# he1.cetak()