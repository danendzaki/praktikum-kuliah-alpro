import datetime

mahasiswa1 = {
    'nama':'ucup',
    'nim':'1234567',
    'sks_lulus':130,
    'beasiswa':False,
    'ttl':datetime.datetime(2000, 1, 1)
}

mahasiswa2 = {
    'nama':'azan maghrib',
    'nim':'13579',
    'sks_lulus':120,
    'beasiswa':True,
    'ttl':datetime.datetime(2001, 4, 4)
}

mahasiswa3 = {
    'nama':'slamet',
    'nim':'24680',
    'sks_lulus':100,
    'beasiswa':True,
    'ttl':datetime.datetime(2002, 7, 7)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<6} {'SKS':<3} {'Beasiswa':<9} {'TTL':<10}")
print("="*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    TTL = data_mahasiswa[KEY]['ttl'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {TTL:<10}")
    
    


 