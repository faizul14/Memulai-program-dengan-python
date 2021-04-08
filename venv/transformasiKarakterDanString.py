#TRANSFORMASI KARAKTER DAN STRING

#mengubah hurup besar/kecil
nama = "faezol"
nama = nama.upper()
print(nama)
nama1 = "FAEZOL PADLI"
nama1 = nama1.lower()
print(nama1)

"""
Menghapus spasi yang tidak perlu atau kata tertenntu
#rstrip()
#lstrip()
#strip()
"""
alamat = "lotim       "
print(alamat.rstrip())

alamat = "       lotim"
print(alamat.lstrip())

alamat = "lotimeuii"
print(alamat.strip("euii"))
alamat = "     lotim       "
print(alamat.strip())

#startswith() -> akan mengembalikan nilai true jika string di awali denagna kata awalan tertentu yang di inginkan
#dan jika tidak maka akan mengambalikan nilai false
print('Dicoding Indonesia'.startswith('Dicoding'))
#endswith() -> kebalikan dari startswith() . akan mengembalikan nilai true jika string yang di akhiri dengan kata akhiran tertentu yang di inginkan
#dan jika tidak akan mengembalikan nilai false
print('Dicoding Indonesia'.endswith('Indonesia'))

#memisaha dan menggabungkan string
#join() -> metode yang di gunakan untuk mfnggabungkan sejumlah string
print(''.join(['Dicoding', 'Indonesia', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))

#split() -> metode yang di gunakan untuk memisahkan substring berdasarkan delimiter tertentu (defaultnya : whitespace
#,tab, atau newline
print('dicoding indonesia'.split())
print('dicoding123indonesia123!'.split('123'))

#MENGGANTI ELEMEN STRING
#replace dapat mengganti kata dalam sebuah kalimat dan bersifat case sensitive
string = "ayo belajar dicoding di Dicoding"
print(string.replace("dicoding", "programing"))

ex2 = "ayo belajar coding di dicoding indonesia karna sekarang ada beasiswa coding digischol dari lintasarta"
print(ex2.replace("coding","programing",1))

#pengecekan string
#isupper -> akan megembalikan nilai true jika semua huruf dalam srtring adalah huruf besar dan false jika terdapat satu
#huruf kecil
kata = "DICODING"
print(kata.isupper())

#islower() -> sebaliknya dari isupper()
kata = 'dicoding'
print(kata.islower())

#isalpha() -> method ini akan mengembalikan nilai true jika semua karakter adalah alfabet
kata = 'dicoding'
print(kata.isalpha())

#isalnum() -> method ini akan mengambalikan nilai true jika semua karakter adalah alfanum (alfabet dan numerik)
kata = 'dicoding123'
print(kata.isalnum())

#isdecimal() -> method ini akan mengembalikan nilai true jika semua karakternya adalah numerik
kata = '12345'
print(kata.isdecimal())

#isspace() -> method ini akan mengmablikan nilai ture jika semua karakternya spasi
kata = '     '
print(kata.isspace())

#istitle() -> method ini akan mengmbalikan nilai turue jika hurruf pertamanya kapital dan hurufselanjutnya huruf kecil
kata = 'Dicoding'
print(kata.istitle())

# while True:
#     print("Masukkan nama anda :")
#     nama = input()
#     if nama.isalpha():
#         print("Selamat datang {}".format(nama) )
#         break
#     print("Masukkan nama anda dengan benar!")

#FORMATING PADA STRING

#zfill() -> methode ini dapat menambhakan angka berupa 0 di sebelah kiri sebuah angka maupun string.
##ini biasanya di pakek untuk nomor antrian atau nomor nota
##dan menambahkan 0 jika value dari zfill() kurang dari angka tsb
##untuk lebih jelasnya silahkan run
#penggunaan zfill() pada angka

angka = 5
##sebelum menggunakan zfill() konversi dulu ke type string
print(str(angka).zfill(5))

angka = 300
print(str(angka).zfill(5))

#penerapan pada string
contoh = 'kamu'
print(contoh.zfill(5))

##TEKS RATA KANAN/KIRI/TENGAH DENGAN rjust(),ljust(),dan center()
##rjust() dan ljust() akan menambahkan spasi atau karakter yang di tentukan untuk membuat rata kanan maupun kiri
##sampai sama jumlahnya denga value yang di kasi

print('dicoding'.rjust(20)) #dengan spasi
print('dicoding'.rjust(20, '!')) #dengan karakter yang di tentukan
print('dicoding'.ljust(20))
print('dicoding'.ljust(20, '!'))
print('dicoding'.center(20))
print('dicoding'.center(20, '-'))

##STRING LITERALS
#jika kita membutuhkan tanda petik di tengah kata seperti hati jum(')at maka ada cara 2 penulisan
#peratama ->kata itu di apit oleh tanda petik2 (")
#kedua dengan backslash (\)
hari = 'hari juma\'at'
print(hari)
hari = "hari juma'at"
print(hari)

#selain tanda kutip dan kutip 2 python juga mempunyai cara penulisan denga kuti 3 yang bisa menampung kalimat lebih
#dari satu bari (multi-line)
hari = """hari ini
adalah hari jum'at dan hari besok 
adalah hari sabtu"""
print(hari)

#RAW STRING
#dengan menulisakn hurf r sebelum pembukaan string maka kalimat itu akn di tampilkan apaadanya
print("faezol\npadli") #tanpa raw string
print(r"faezol\npadli") #denga raw string

