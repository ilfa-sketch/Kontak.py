kontak = [
    {"Nama" : "budi",
     "nomor": 1212,
     "email": "budi@gmail.com"
    },
    {"Nama" : "aisah",
     "nomor": 4545,
     "email": "aisah@gmail.com"
    },
    {"Nama" : "fahran",
     "nomor": 7676,
     "email": "fahran@gmail.com"
    },
    {
     "Nama" : "faruq",
     "nomor": 8989,
     "email": "faruq@gmail.com"
    }]

def tampilkan_kontak() :
    for i, item in enumerate(kontak):
        print(f"{i + 1}.Nama : {item["Nama"]}")
        print(f"  Nomor : {item["nomor"]}")
        print(f"  Email : {item["email"]}\n")

def tambah_kontak() : 
    index = int(len(kontak))
    kontak_baru = {}
    while True :
        Nama_baru = input("Masukkan nama: ").strip()
        if all(c.isalpha() or c.isspace() for c in Nama_baru) and Nama_baru:
            print(f"Nama di buat : {Nama_baru}")
            kontak_baru['Nama']= Nama_baru
            break
        elif Nama_baru.isdigit():
            print("masukkan nama yang benar")
            continue
        else: 
            print("masukkan nama yang benar")
            continue
    while True :
        nomor_baru = input("masukkan nomor : ")
        if nomor_baru.isdigit() :
            print(f"nomor di tambahkan :{nomor_baru}")
            kontak_baru['nomor'] = nomor_baru
            break
        elif nomor_baru.isalpha() :
            print("no")
            continue
        else : 
            print("no") 
            continue
    email_baru = input("masukkan email : ")
    kontak_baru['email'] = email_baru + '@gmail.com'
    kontak.append([])
    kontak[index] = kontak_baru

def hapus_kontak() :
    while True :
        input_user = input("kontak nomor berapa yang ingin anda hapus??: ")
        if input_user.isdigit():
            convert = int(input_user)
            if convert <= len(kontak) and convert != 0:
                kontak.pop(convert - 1)
                break
            else:
                print("masukkan index atau angka yang benar")
                continue
        elif not input_user:
            print("input kosong")
            continue
        else:
            print("masukkan nomor yang benar")
            continue
            

def ubah_nama(index):
    while True :
        input_nama = input("Nama baru >> ")
        if all(c.isalpha() or c.isspace() for c in input_nama) and input_nama:
            kontak[index-1]["Nama"] = input_nama
            break
        else :
            print("masukkan index yamg benar!!!")
            continue

def ubah_nomor(index):
    while True :
        input_nomor = input("nomor baru >> ")
        if input_nomor.isdigit():
            convert = int(input_nomor)
            kontak[index-1]["nomor"] = convert
            break
        else:
            print("masukkan nomor yang benar!!")
            continue

def ubah_email(index):
    input_email = input("Masukkan nama email baru >>") + "@gmail.com"
    kontak[index-1]["email"] = input_email


def edit_kontak() :
    while True :
        user_input = input("Kontak berapa yg ingin anda edit?? ")
        convert = int(user_input)
        if user_input.isdigit() and convert <= len(kontak) and convert != 0:
            print("INGIN MENGUBAH APA??\n1. Nama\n2. Nomor\n3. Email")
            input_user_change = int(input(">> "))
            if input_user_change == 1:
                ubah_nama(convert)
                break
            elif input_user_change == 2:
                ubah_nomor(convert)
                break
            elif input_user_change == 3:
                ubah_email(convert)
                break
            else :
                print("masukkan angka yg sesuai")
                continue
        else:
            print("Masukkan angka atau index yang sesuai")
            continue

while True :
    print(f"\n\n{" "*5} KONTAK")
    tampilkan_kontak()
    print("PILIHAN :\n1. Tambahkan kontak\n2. Hapus kontak\n3. edit kontak\n4. keluar")
    user_input = input(">> ")
    convert = int(user_input)
    if user_input.isdigit and convert <= 4 and convert != 0:
        if convert == 1 :
            tambah_kontak()
            continue
        elif convert == 2 :
            hapus_kontak()
            continue
        elif convert == 3 :
            edit_kontak()
            continue
        else :
            print("EXIT")
            break
    else :
        print("Masukkan index yang benar")
        continue
        