##untuk memasukkan nilai variabel pada string python mempunyai 2 cara
#1. langsung menggabungkan pada statment
x = 100
print('nilai x adalah ',x)
#dan bisa menggunakan string format
print('hai {}'.format('bro'))

#2. mengguanakan operator % yang di tambahkan dengan argumen specifier
# %s - string
# %d - integer
# %f - bilangan
# %.<digit>f - bilangan desimal dengan sejumlah digit angka belakang koma
# %x/%X - bilangan bukat dalam representsai hexa
nama = 'dicoding'
umur = 5
print('nama saya %s dan umur %d tahun.'%(nama, umur))
a,b = 10, 11
a, b
print('a : %x dan b: %X'%(a,b))

#dan untuk menjumlahkan angka yang ada di dala string mengguanakn eval()
#print(int('9+2')) #ini akan error
print(eval('9+2'))