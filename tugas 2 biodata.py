npm = int(input("Masukkan NPM: "))
nama = input("Masukkan Nama: ")
tinggi = float(input("Masukkan Tinggi Badan: "))
prodi = input("Masukkan Prodi: ")

tugas = float(input("Masukkan Nilai Tugas: "))
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))

nilai_akhir = (tugas + uts + uas) / 3

print("\n=== DATA MAHASISWA ===")
print("NPM         :", npm)
print("Nama        :", nama)
print("Tinggi      :", tinggi)
print("Prodi       :", prodi)

print("\n=== NILAI ===")
print("Tugas       :", tugas)
print("UTS         :", uts)
print("UAS         :", uas)
print("Nilai Akhir :", nilai_akhir)

if nilai_akhir >= 75:
    print("Anda Lulus")
else:
    print("Anda Tidak Lulus")