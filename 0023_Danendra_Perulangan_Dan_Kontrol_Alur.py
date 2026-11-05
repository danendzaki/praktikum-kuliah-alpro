# Bilangan ganjil
angka = 0
while angka < 50:
    angka += 1
    if angka % 2 == 0:
        continue
    print(angka)
    
# Bilangan genap
angka = 0
while angka < 50:
    angka += 1
    if angka % 2 != 0:
        continue
    print(angka) 
    
# Bilangan prima
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)