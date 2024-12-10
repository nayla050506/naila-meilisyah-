# percabangan
# struktur 
"""
    1. if -nya
    2. punya kondisi
    3. punya aksi
"""
nama = input ("Masukkan Nama : ")

# percabangan yang inline (satu baris)
if nama == "adam" : print ("Selamat Datanf")
print ("Terimakasih")

# percabangan indentasi
if nama == "adam" :
    print ("Selamat Datang")
    print ("Selamat Belajar Python")
print ("Bukan Bagian Percabangan")

# percabangan  1 kondisi dan 2 aksi
# pakai kata kunci 'else'

if nama == "adam" :
    print (f'Selamat Datang {nama}')
else:
    print (f'Anda {nama}, bukan adam')
print ("Terima Kasih")