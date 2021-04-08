#List - adalah sekumpulan data terurut yang sering di pakai di python . serupa tapi tak sama dengan array
#elemen list pada python tidak harus memiliki type data yang sama
a = [1, "python", 2.3]
print(a)

#slicing - dapat mengambil data per index
# x[0] - mengambil data paling awal pada index ke 0
# x[n] - mengambil data pada index ke n
# x[-1] - mengmabil data paling akhir
# x[3:5] - membuat list dari elemen list x yang memmulai dari index ke 3 sampai sebelum index 5
# x[:5] - membuat list dari elemen x yang memulai dari paling awal sampai sebelum inedex ke 5
# x[-3:] - membuat list dari elemen x yang di mulai dari index ke 3 terahir hingga paling index paling ahir
# x[1:7:2] - membuat list dari elemen x yang di mulai dari index ke 1 sampai sebelum index ke 7 dengan step 2

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(x[0])
print(x[-1])
print(x[5])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

# untuk menambahkan elemen pada list menggunakan append()
x.append(55)
print(x)
# untuk menghapus elemen pada list menggunanak del x[2]
del x[-1]
print(x)

# slicing juga bisa di gunakan di string
kalimat = "Hello Dunia"
print(kalimat[2]) #dst kalian berkreasi sessuai panduan slicing dia atas ya :)

#TUPLE - jenis dari list yang tidak dapat di ubah elemennya
t = (5, "program", 3+5j)
print(t)
print(t[2])
#t[2] = 23 #ini akan error

#SET - kumpulan item bersifat unik tanpa urutan dan di definisikan dengan kurawal
# pada set kita dapat melakukan union dan intersection, dekaligus melakukan penghapusan data duplikat
a = {1, 2, 2, 2, 3, 4, 5, 4, 2}
print(a)
#karna bersifat tidak terurut maka tidak bisa melakukan slicing
#print(a[1]) # ini akan erorr

#DICTIONARY - pada pyhton adalah kumpulan key-value
# key bisa integer atau string begitu juga value nya bisa integer atau string
d = {1:'va', 'umur':5, 'nama':'faezol', 3:3 }
print(d['nama'])
print(d[3])