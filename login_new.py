users = {}
status = ""

def displayMenu():
    print()
    status = str(input("Apa yang ingin anda lakukan?\nKetik y = daftar dan n = login dan q = keluar: ")) 
    if status == "y":
        newUser()
    elif status == "n":
        oldUser()
    elif status == "q":
        exit()

def newUser():
    print()
    createLogin = input("Masukkan Nama: ")
    telephone = input("Masukkan No Telepon: ")
    email = input("Masukkan Email: ")

    if createLogin in users: 
        print("\nNama sudah tersedia!\n")
    else:
        createPassw = input("Masukkan Password: ")
        users[createLogin] = createPassw
        print("\nUser sudah terdaftar!\n")     

def oldUser():
    print()
    login = input("Nama: ")
    passw = input("Password: ")

    if login in users and users[login] == passw: 
        print("Login berhasil!")
    elif not (login == str) or (passw == int):
        print("Nama hanya boleh berisi huruf!")
        print("Password hanya bisa diisi dengan angka!")
    else:
        print("User tidak ditemukan atau password salah!")

while status != "q":            
    displayMenu()