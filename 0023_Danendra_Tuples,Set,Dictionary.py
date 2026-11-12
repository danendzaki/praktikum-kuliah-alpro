mahasiswa = ("Danendra Dzaki Andita", "2605060023", "Teknologi Informasi")

print("NIM:", mahasiswa[1])
print("Prodi:", mahasiswa[2])

nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026

del data_mahasiswa["nim"]

print(data_mahasiswa)

keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

total = 0

for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")
    total += harga

print(f"Total belanja: Rp {total}")