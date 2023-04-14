import datetime
import os

data_buku = {
    'penulis':'XXXXXXXxXXX',
    'judul':'xxxxxxxx',
    'Publikasi':datetime.datetime(2020,11,10)
}

data_perpus = {}

while True : 
	buku = dict.fromkeys(data_buku.keys())
	buku['penulis'] = input("Nama pengarang : ")
	buku['judul'] = input("judul buku: ")
	TAHUN_PUBLIKASI = int(input("Tahun publikasi (YYYY): "))
	BULAN_PUBLIKASI = int(input("Bulan publikasi (1-12): "))
	TANGGAL_PUBLIKASI = int(input("Tanggal publikasi (1-31): "))
	buku['Publikasi'] = datetime.datetime(TAHUN_PUBLIKASI,BULAN_PUBLIKASI,TANGGAL_PUBLIKASI)

	KEY = input("Masukkan Urutan : ")
	data_perpus.update({KEY:buku})
	print(data_perpus)
	print(f"\n{'KEY':<6} {'Penulis':<17} {'Judul':<10} {'Publikasi':<10}")
	print('-'*60)

	for KEY in data_perpus:
		pengarang = data_perpus[KEY]['penulis']
		judul = data_perpus[KEY]['judul']
		tahun_publikasi = data_perpus[KEY]['Publikasi'].strftime("%x")
		print(f"{KEY:<6} {pengarang:<17} {judul:<10} {tahun_publikasi:<10}")

	is_done = input("\nTambah lagi? (y/n) : ")
	if is_done == 'n' : 
		break
print("\n")
print("program selesai")
