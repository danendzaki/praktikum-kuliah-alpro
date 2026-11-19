import datetime

mahasiswa_template = {
    'nama':'nama',
    'nim':0000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111, 1, 1)
}

data_mahasiswa = {}

print(f"{'Selamat Datang':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("="*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
ttl = input("Tanggal Lahir (dd-mm-yyyy): ")
mahasiswa['lahir'] = datetime.datetime(ttl)

print(mahasiswa)

