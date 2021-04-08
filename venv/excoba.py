import  os

username = ["fuu"]
password = ["34"]
pass1 = ""
datake = 0

op = input("Selamat datang di system saya : \n"
      "apakah sudah login??\n"
      "1. YA\n"
      "2. BELUM\n"
      ">> ")

def logpass():
    panjang = len(password)
    for i in range[0:panjang]:
        if password[i] == pass1:
            datake = i
            break


def login():
    username1 = input("masukkan username anda >>")
    password1 = input("masukkan password anda >>")
    if username1 in username :
        logpass()
        if password1.lower() == password[datake]:
            print("selamat anda berhasil login")
    else:
        print("username tidak ada ")
def daf():
    print("anda belum terdaftar! silahkan daftarkan diri anda -_-")
    nama = input("masukkan username >>")
    passs = input("masukkan password >>")
    username.append(nama)
    password.append(passs)


while True:
    if op == 1:
        login()
        break
    else:
        daf()
        op = 1
