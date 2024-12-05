from gempa import *

# Membuat objek
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)


# Info Gempa
print()
gempa1.dampak() #menampilkan panggil yang di method dampak di file gempa
print('##Info 1##')
print()
gempa2.dampak()
print('##Info 2##')
print()
gempa3.dampak()
print('##Info 3##')
print()
gempa4.dampak()
print('##Info 4##')
print()
gempa5.dampak()
print('##Info 5##')