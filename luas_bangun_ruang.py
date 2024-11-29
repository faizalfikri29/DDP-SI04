def l_kubus(sisi):
    luas = 6 * sisi * sisi
    print(f'Luas Kubus 6 * {sisi} * {sisi} = {luas}')

def l_tabung(r1,t):
    luas = 2 * 3.14 * r1 * (r1+t)
    print(f'Luas Tabung 2 * phi * {r1} * ({r1} + {t}) = {luas}')

def l_balok(p,l,t):
    luas = (2 * p * l) + (2 * p * t) + (2 * l * t)
    print(f'Luas Balok dari {p}, {l}, {t} adalah {luas}')

def l_bola(r1,r2):
    luas = 4 * 3.14 * r1 * r2
    print(f'Luas bola 4 * phi * {r1} * {r2} = {luas}')

def l_kerucut(r, s):
    luas = 3.14 * r * (r + s)
    print(f'Luas Permukaan Kerucut phi * {r} * ({r} + {s}) = {luas}')