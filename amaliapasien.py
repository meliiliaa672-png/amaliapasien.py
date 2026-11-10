print("==================================================")
print("            RUMAH SAKIT SEHAT SEJAHTERA           ")
print("==================================================")

nama_pasien = input("Masukkan Nama Pasien: ")

print("\nDAFTAR PENYAKIT PASIEN:")
print("1. Demam Berdarah (DBD)")
print("2. Tifus (Typhoid)")
print("3. Diabetes Melitus")
print("4. Hipertensi (Tekanan Darah Tinggi)")
print("5. Pneumonia (Paru-paru)")
print("6. Gastroenteritis (Muntaber)")
print("7. Asthma Bronkial")
print("8. Cedera Ringan / Trauma")
print("9. Anemia Berat")
print("10. Maag Kronis")
print("11. Gagal Ginjal")
print("12. Infeksi Saluran Kemih (ISK)")

pilihan_penyakit = int(input("\nPilih nomor penyakit (1-12): "))

print("\nPILIHAN KELAS PERAWATAN:")
print("1. VIP (Fasilitas: 1 Bed, AC, TV, Kulkas, Sofa, Kamar Mandi Dalam, Makan 3x)")
print("2. Kelas 1 (Fasilitas: 2 Bed, AC, TV, Kamar Mandi Dalam, Makan 3x)")
print("3. Kelas 2 (Fasilitas: 4 Bed, Kipas/AC, TV Bersama, Kamar Mandi Dalam, Makan 3x)")
print("4. Kelas 3 (Fasilitas: 6 Bed, Kipas Angin, Kamar Mandi Luar, Makan 3x)")

pilihan_kelas = int(input("Pilih nomor kelas perawatan (1-4): "))
lama = int(input("Masukkan lama opname (hari): "))

if pilihan_penyakit == 1:
    penyakit = "Demam Berdarah (DBD)"
    harga_dasar = 450000
elif pilihan_penyakit == 2:
    penyakit = "Tifus (Typhoid)"
    harga_dasar = 400000
elif pilihan_penyakit == 3:
    penyakit = "Diabetes Melitus"
    harga_dasar = 550000
elif pilihan_penyakit == 4:
    penyakit = "Hipertensi (Tekanan Darah Tinggi)"
    harga_dasar = 350000
elif pilihan_penyakit == 5:
    penyakit = "Pneumonia (Paru-paru)"
    harga_dasar = 600000
elif pilihan_penyakit == 6:
    penyakit = "Gastroenteritis (Muntaber)"
    harga_dasar = 350000
elif pilihan_penyakit == 7:
    penyakit = "Asthma Bronkial"
    harga_dasar = 400000
elif pilihan_penyakit == 8:
    penyakit = "Cedera Ringan / Trauma"
    harga_dasar = 500000
elif pilihan_penyakit == 9:
    penyakit = "Anemia Berat"
    harga_dasar = 450000
elif pilihan_penyakit == 10:
    penyakit = "Maag Kronis"
    harga_dasar = 350000
elif pilihan_penyakit == 11:
    penyakit = "Gagal Ginjal"
    harga_dasar = 800000
elif pilihan_penyakit == 12:
    penyakit = "Infeksi Saluran Kemih (ISK)"
    harga_dasar = 400000
else:
    penyakit = ""
    harga_dasar = 0

if pilihan_kelas == 1:
    kelas = "VIP"
    pengali = 2.5
    kunjungan = "Pukul 10.00 - 20.00 WIB (Maks. 3 Pengunjung)"
elif pilihan_kelas == 2:
    kelas = "Kelas 1"
    pengali = 1.8
    kunjungan = "Pukul 11.00 - 13.00 & 16.00 - 19.00 WIB (Maks. 2 Pengunjung)"
elif pilihan_kelas == 3:
    kelas = "Kelas 2"
    pengali = 1.4
    kunjungan = "Pukul 11.00 - 12.00 & 17.00 - 18.30 WIB (Maks. 2 Pengunjung)"
elif pilihan_kelas == 4:
    kelas = "Kelas 3"
    pengali = 1.0
    kunjungan = "Pukul 16.00 - 18.00 WIB (Maks. 1 Pengunjung Bergantian)"
else:
    kelas = ""
    pengali = 0
    kunjungan = ""

if (1 <= pilihan_penyakit <= 12) and (1 <= pilihan_kelas <= 4) and (lama >= 1):
    biaya_per_ihari = int(harga_dasar * pengali)
    total_biaya = biaya_per_ihari * lama

    print("\n" + "=" * 50)
    print("                 STRUK RINCIAN BIAYA RS                   ")
    print("=" * 50)
    print("Nama Pasien     :", nama_pasien)
    print("Diagnosa        :", penyakit)
    print("Kelas Perawatan :", kelas)
    print("Lama Opname     :", lama, "hari")
    print("Jadwal Kunjungan:", kunjungan)
    print("-" * 50)
    print("Biaya per Hari  : Rp", biaya_per_ihari)
    print("Total Biaya     : Rp", total_biaya)
    print("-" * 50)

    if lama > 7:
        print("Status Opname   : Opname Panjang (Perlu Evaluasi Berkala)")
    else:
        print("Status Opname   : Opname Standar / Normal")
    print("=" * 50)
else:
    print("\n[Peringatan] Data yang Anda masukkan tidak valid (Pilihan penyakit/kelas/lama opname salah).")