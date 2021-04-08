#if - pada python seperti pada percabnagan lainnya
#pada python >0 mengmbalikan nilai true dan 0 mengenmbak=likan nilai false
kelereng = 10
if kelereng:
    print("cetak ini jika benar")
    print(kelereng)

#else - statment else dapat di kombinasikan dengan if. sebagai jalan keluar saat kondisi if benilai false
tinggi_badan = int(input("masukkan tinggi badan anda >>"))
if tinggi_badan >= 160:
    print("silahkan anda boleh masuk")
else:
    print("anda tidak boleh masuk")
#ex 2
bilangan = 4
if 4 % 2 == 0:
    print("bilangan %d adalah bilangna genap"%bilangan)
else:
    print("bilangan %d adalah bilangan ganjil"%bilangan)

#elif - adalah singkatan dari else if dan alternatife utnuk if bertingkat
nilai = int(input("masukkan nilai yang anda dapat >>"))
if nilai >= 80:
    print("Grade anda A")
    print("nice anda hebat")
elif nilai >= 70:
    print("Grade anda B")
    print("masi bagus, nice")
elif nilai >= 60:
    print("Grade anda C")
    print("nice dan tingkatkan ya.. .")
else:
    print("Grade anda D")
    print("wah perlu di tingkatkan belajarnya ini bung")

#Ternary operator - lebih di kenal dengan k=conditional expresion di python .jika statment atau kondisi anda sederhana
#bisa menggunakan ternary operator
kondisi = True
print( 2 if kondisi else "ini jika kondisi false")

#shorthand ternary - membantu anda memeriksa hasil fungsi dan memastikan outputnya tidak menyebabkan error
hasil = None
pesan = hasil or "tidak ada data bung"
print(pesan)

