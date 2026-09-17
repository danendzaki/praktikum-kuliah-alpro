usia = int(input("Masukkan usia Anda: "))

if usia < 12:
    print("Anda adalah anak-anak.")
elif usia > 13 and usia < 20:
    print("Anda adalah remaja.")
elif usia > 18 and usia < 59:
    print("Anda adalah dewasa.")
else :
    print("Anda adalah lansia.")

