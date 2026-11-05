status_akun = "aktif"
saldo = 1000000
nominal_tarik = int(input("Masukkan nominal penarikan: Rp"))

if status_akun == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 50000:
            saldo = saldo - nominal_tarik
            print(f"Penarikan berhasil: Rp{nominal_tarik:,} ")
            print(f"Sisa saldo: Rp{saldo:,} ")
        else:
            print("Nominal penarikan minimal Rp50.000")
    else:
        print("Saldo tidak mencukupi")
else:
    print("Akun tidak aktif")
    
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("Teknologi Informasi")
        j += 1
    print("\n")
    i += 1
    
i = 1
N = 1

while i <= 2:
    j = 1
    while j <= 3:
        print(N)
        N = N + 2
        j += 1
    i += 1
    
sesi = 1
while sesi <= 2:
    print(f"Sesi ke-{sesi}:")
    
    for antrian in range(1, 4):
        print(f"  Melayani pasien nomor")