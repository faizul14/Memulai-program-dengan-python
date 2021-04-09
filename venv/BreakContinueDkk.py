#break - pernyataan break mnghentika perulangan kemudian keluar, dan megekskusi statmen di blok setelah
#perulangan tsb

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('huruf saat ini : {}'.format(huruf))

#CONTINUE - pernyataan continue akan membuat iterasi saat in berhenti dan melanjutkan ke iterasi ke selanjutnya
for huruf in 'dico ding':
    if huruf == ' ':
        continue
    print('huruf saat ini : %s'%huruf)
    ## Note -> perhatikan outputnya = yang spasi di abaikan


#Else setelah for - fungsinya di utamakna untuk pencarian - untuk menjadi jalan keluar program saat data tidak
# di temukan
items = [2, 3, 55, 66, 4]
for item in items:
    if item == 55:
        print("data di temukan!")
        break
else:
    print("data tidak di temukan")
# jika kondisi if mendapatkan kodisi true sekali saja makan else setelah for tidak akan di ekskusi
for i in range(2, 10):
    pass
    # n = i
    # for x in range(2, n):
    #     if n % x == 0 :
    #         print(n, 'equals', x, '*', n/x)
    #         break
    # else:
    #     print(n, 'adalah bilangan prima' )

#Else setelah while - berbeda dengan for , else akan selalu di ekskusi jika kondisi while bernilai false
n = 10
while n > 0 :
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print('loop selesai')

#Pass - di gunakan saat menginginkan statment atau blok tidak melakukan apa2 suaoaya tidak error
#biasanya sering di gunakan saat belum melakukan implementasi
def sebuah_fungsi():
    pass # jika passnya di hilangin maka akan terjadi error
