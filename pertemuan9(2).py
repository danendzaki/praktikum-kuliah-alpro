
# Contoh Nesting Dictionary

data_mahasiswa = {
    "2605060023": {
        "nama": "Danendra",
        "prodi": "Teknologi Informasi",
        "angkatan": 2026
    },
    "2605060024": {
        "nama": "Andi",
        "prodi": "Teknik Sipil",
        "angkatan": 2026
    }
}

print("DATA MAHASISWA")
print("-" * 35)

for nim, mahasiswa in data_mahasiswa.items():
    print(f"NIM: {nim}")
    print(f"Nama: {mahasiswa['nama']}")
    print(f"Prodi: {mahasiswa['prodi']}")
    print(f"Angkatan: {mahasiswa['angkatan']}")
    print()

print("Nama mahasiswa:", data_mahasiswa["2605060023"]["nama"])
