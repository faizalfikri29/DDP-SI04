class Gempa:
    # Konstruktor inisialisasi
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Membuat Penentu skala Gempa
    def dampak(self):
        # statement/logika
        if self.skala < 2:
            print('Gempa Tidak berasa')
        elif self.skala <= 4:
            print('gempa bangunan retak-retak')
        elif 4 <= self.skala <=6:
            print('gempa bangunan roboh')
        elif self.skala > 6:
            print('gempa bangunan roboh dan berpotensi tsunami')

        # Menampilkan lokasi dan skala gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'skala Gempa: {self.skala}')