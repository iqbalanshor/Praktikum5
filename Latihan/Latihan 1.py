from prettytable import PrettyTable

# Buat dictionary daftar kontak
daftar_kontak = {
    'Ari': '081234567',
    'Dina': '082345678',
    'Eva': '083456789'
}

# Tampilkan kontak Ari
print("Kontak Ari:", daftar_kontak.get('Ari', 'Kontak tidak ditemukan'))

# Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak['Riko'] = '087654544'

# Ubah kontak Dina dengan nomor baru 088999776
daftar_kontak['Dina'] = '088999776'

# Tampilkan semua Nama
print("Semua Nama:")
for nama in daftar_kontak.keys():
    print(nama)

# Tampilkan semua Nomor
print("\nSemua Nomor:")
for nomor in daftar_kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan nomornya
print("\nDaftar Nama dan Nomor:")
table = PrettyTable(['Nama', 'Nomor'])
for nama, nomor in daftar_kontak.items():
    table.add_row([nama, nomor])
print(table)

# Hapus kontak Dina
if 'Dina' in daftar_kontak:
    del daftar_kontak['Dina']

# Tampilkan hasil setelah menghapus Dina
print("\nSetelah menghapus Dina:")
table = PrettyTable(['Nama', 'Nomor'])
for nama, nomor in daftar_kontak.items():
    table.add_row([nama, nomor])
print(table)
