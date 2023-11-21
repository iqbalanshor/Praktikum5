data_mahasiswa = {}

while True:
    data = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    if data.lower() == 't':
        print("Tambah Data")
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        tugas = int(input("Nilai Tugas    : "))
        uts = int(input("Nilai UTS      : ")) 
        uas = int(input("Nilai UAS      : "))
        nilaiakhir = tugas * 0.3 + uts * 0.35 + uas * 0.35
        data_mahasiswa[nama] = nim, tugas, uts, uas, nilaiakhir

    elif data.lower() == 'u':
        print("Ubah Data")
        nama = input("Masukkan Nama  : ")
        if nama in data_mahasiswa.keys():
            nim = int(input("NIM            : "))
            tugas = int(input("Nilai Tugas    : "))
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            nilaiakhir = tugas * 0.3 + uts * 0.35 + uas * 0.35
            data_mahasiswa[nama] = nim, tugas, uts, uas, nilaiakhir
        else:
            print("Nama {0} tidak ditemukan".format(nama))

    elif data.lower() == 'h':
        print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in data_mahasiswa.keys():
            del data_mahasiswa[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    elif data.lower() == 'c':
        print("Cari Data")
        nama = input("Masukkan Nama : ")
        if nama in data_mahasiswa.keys():
            print("="*79)
            print("|                                Daftar Mahasiswa                             |")
            print("="*79)
            print("| Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
            print("="*79)
            print("| {0:15s} | {1:15d} | {2:7d} | {3:5d} | {4:5d} | {5:9.2f}     |"
                  .format(nama, nim, tugas, uts, uas, nilaiakhir))
            print("="*79)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    elif data.lower() == 'l':
        if data_mahasiswa.items():
            print("="*84)
            print("|                                  Daftar Mahasiswa                                |")
            print("="*84)
            print("|No. | Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
            print("="*84)
            i = 0
            for z in data_mahasiswa.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:7d} | {3:5d} | {4:5d} | {5:9.2f}     |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 84)
        else:
            print("="*84)
            print("|                                  Daftar Mahasiswa                                |")
            print("="*84)
            print("|No. | Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
            print("="*84)
            print("|                                   TIDAK ADA DATA                                 |")
            print("="*84)

    elif data. lower() == 'k':
        print("=====| Keluar |=====")
        break

    else:
        print("Pilih menu yang tersedia")