##len() -> adalha untuk menghitung panjang list,set,tuple dan string
data_list = [1,2,3,4,5,6,7,8,9]
print(data_list)
print(len(data_list))

data_set = (1,2,3,4,5,6,7,8,9,9)
print(data_set)
print(len(data_set))

contoh_string = "saya mendapat token dari digital scholl utntuk belajar di Dicoding indonesia"
print("jumlah karakter : {}".format(len(contoh_string)))

#min() dan max() ->adalah method yang di gunakan untuk mengetahui angka terbesar atau terkecil dalam list dkk
contoh_list2 = [1,90,1000,199,90,78,1098,11]
print(min(contoh_list2))
print(max(contoh_list2))

#count() -> utntuk mengetahui berapa kali objek itu muncul , di dalam list maupun string
contoh_list3 = [1, 2, 2, 4, 4, 5, 2, 4, 5]
print(contoh_list3.count(2))
contoh_string = "saya mendapat token dari digital scholl utntuk belajar di Dicoding indonesia"
print(contoh_string.count('a'))

##PENGGABUNGAN DAN REPLIKASI
#dimungkinkan menggunakan operasi tambah(+) dan kali(*)
angka = [1,2,3,4,5]
huruf = "python"
huruf = list(huruf.upper())
print(huruf)
gabung = angka + huruf
print(gabung)

#replikasi
learn = huruf
replikasi = learn * 2
print(replikasi)
print(len(replikasi))
print(replikasi[0:6])
#dan bisa juga untuk inisialisasi list
a = [8] * 8
print(len(a))
print(a)

#RANGE  -> dengan 1 parameter yang akan di mulai dari 0
for i in range(5):
    print("{} ".format(i))
#RANGE -> dengan 2 parameter n,p:
#yang mana mulai dari n dan berhenti sebelum p
print("ini range yang 2 parameter")
for i in range(1, 11):
    print(i)
#RANGE dengan 3 parameter n,p,q:
#yang mana di mulai dari n, berhenti sebelum p, dan setiap elemen memiliki selisih q
print("ini range yang 3 parameter ")
for i in range(1, 20, 5):
    print(i)

#in dan not in -> yaitu mengembalika nilai true dan false
#berfungsi untuk mengetahui nilai objek ada dalam list dan string
kalimat = "belajar python di dicoding sangat menyenangkan"
print('dicoding' in kalimat)
print('digi' not in kalimat)

#MEMBERIIAKN NILAI UTNTUK NILAI VARIABEL
data_baju = ['jeans', "89000", "L"]
jenis, harga, size = data_baju
print(jenis + harga + size)

#short() -> untuk mengurutkan angka atau alfabet
#dan tidak bisa mengurutkan list yang berisi int dan string sekaligus
angka = [88,5,1,90,7,6]
angka.sort()
print(angka)
#untuk mengurutkan nilai dari yang terahir maka value (reverse=true) pada method sort()
angka.sort(reverse = True)
print(angka)
alfabet = ["motor", "mobil", "helikopter","pesawat"]
alfabet.sort()
print(alfabet)
#metode sort() menggunakan urutan ASCII, sehingga huruf kapital akan lebih dahulu di bandingkan huruf kecil
alfabet = ["motor", "Mobil", "helikopter","pesawat"]
alfabet.sort()
print(alfabet)
#nah untuk mengatasi kendala ini bisa kita masukkan keyword (str.lower) pada paramaeter
alfabet = ["motor", "Mobil", "helikopter","pesawat"]
alfabet.sort(key=str.lower)
print(alfabet)