angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

angka2 = [1, 2, 3, 4,] 
print(angka2)

for i in angka2: 
    print(f"i sekarang → {i}")
print("Akhir dari perulangan\n")

angka3 = range(5)

for i in angka3:
    print(f"i sekarang → {i}")
print("Akhir dari perulangan\n")

angka4 = range(1, 10)
for i in angka4:
    print(f"i sekarang → {i}")
print("Akhir dari perulangan\n")

data_str = "saya ganteng"

for huruf in data_str:
    print(huruf)
print("Akhir dari program\n")

print("==contoh1==\n")

# angka = 10
# while angka > 5:
#     print("ipin lari ipin!")
    
print("==contoh2==\n")

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang → {angka}")
    print("ipin lari ipin!")
    
print("program selesai, ipin sudah jauh")

angka = 0
while angka < 5:
    angka = angka + 1
    
    if (angka == 3):
        print(angka)

angka = 0 
print(f"angka sekarang → {angka}")

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}")
    
    if angka == 3:
        print("print")
        continue
    print("wassap")
print("finish")

