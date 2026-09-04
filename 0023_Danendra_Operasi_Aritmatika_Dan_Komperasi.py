panjang = 12
lebar = 5
tinggi = 8

luas = panjang * lebar
print("Luas Persegi Panjang = ", luas)

volume = panjang * lebar * tinggi
print("Volume Balok = ", volume)

keliling = 2 * (panjang + lebar)
print("Keliling Persegi Panjang = ", keliling)

if luas > 50:
    print(bool(luas > 50), ", luas dari persegi lebih dari 50")
else:
    print(bool(luas > 50), ", luas dari persegi tidak lebih dari 50")
    
if volume == 480:
    print(bool(volume == 480), ", volume dari balok sama dengan 480")
else:
    print(bool(volume == 480), ", volume dari balok tidak sama dengan 480")