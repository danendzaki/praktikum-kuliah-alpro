kendaraan =["motor","mobil", "sepeda", "bus"]
kendaraan.append("truk")
print(f"kendaraan Truk telah ditambahkan ke dalam list kendaraan: \n{kendaraan}")

kendaraan.insert(1,"becak")
print(f"Kendaraan becak telah ditambah pada data kendaraan pada index 1: \n{kendaraan}")

kendaraan.pop()
print(f"kendaraan bus telah dikeluarkan dari list kendaraan: \n{kendaraan}")

kendaraan[2] = "skuter"
print(f"kendaraan sepeda telah diganti menjadi skuter: \n{kendaraan}")

total_list_kendaraan = len(kendaraan)
print(f"Panjang list kendaraan adalah: {total_list_kendaraan}")

angka = [75, 80, 90, 75, 85, 100, 65]
print(f"nilai 100 ada pada index ke-{angka.index(100)}")

print(f"siswa yang medapat nilai 75 sebanyak {angka.count(75)} orang")

print(f"list skor dari yang terkecil hingga yang terbesar: {sorted(angka)}")

angka.reverse()
print(f"list skor dari yang terbesar hingga yang terkecil: {angka}")


menu_utama = ["Nasi goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"Menu utama dan menu tambahan digabungkan menjadi: {menu_utama}")


