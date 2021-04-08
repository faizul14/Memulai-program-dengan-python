#for - pada python seperti perulangan for pada bahasa lain namun for di python tidak hanya untuk sekumpulan data saja
#namun bisa untuk variabel

for i in "dicoding":
    print(i)

anime = ["aot", "kimi no uso", "naruto", "kimi no yaiba", "boku no hero"]
for i in range(len(anime)):
    print(anime[i])
#while - mengekskusi statment selama kindisi while terpenuhi
#TIPS ## python tidak memiliki do.. while
c = 0
while c < 7:
    print("ini data ke {}".format(c))
    c += 1

#perulangan bertingkat
for i in range(0, 6):
    for j in range(0, 6-i):
        print("*", end='')
    print()