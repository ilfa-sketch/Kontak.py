class Menu:
    def __init__(self):
        with open("kontak.txt",mode="r") as var:
            self.content = [line.strip().split(',') for line in var.readlines()]
    
    def tampilkan_semua_kontak(self):
        if len(self.content) == 0:
            print("CONTACT IS EMPTY")
            return 1
        else:
            for i,item in enumerate(self.content,start=1):
                print(f"{i}.{item[1]} : {item[3]}")
            return 2
        
        
    def tampilkan_kontak_spesifik(self,input):
        kontak = self.content[input-1]
        print(f"Nama : {kontak[1]}\nEmail : {kontak[2]}\nNomor hp: {kontak[3]}")
        
    def edit_kontak(self):
        while True:
            inputUser = input("INGIN MENGEDIT NO BERAPA??\n>> ")
            if inputUser.isdigit():
                convert = int(inputUser)
                if convert > 0 and convert <= len(self.content):
                    self.tampilkan_kontak_spesifik(convert)
                    self.pilihan_menu_edit_kontak(convert)
                    break
                else:
                    print(f"MASUKKAN NOMOR 1 - {len(self.content)}")
                    continue
            else:
                print("MASUKKAN INPUT NUMBER")
                continue
                
    def pilihan_menu_edit_kontak(self,numb):
        while True:
            print("EDIT : \n1. NAMA\n2. EMAIL\n3. NOMOR")
            inputUser = input(">> ")
            if inputUser.isdigit():
                convert = int(inputUser)
                if convert > 0 and convert < 4:
                    if inputUser == 1:
                        self.ganti_nama(numb)
                        break
                    elif inputUser == 2:
                        self.ganti_email(numb)
                        break
                    else:
                        self.ganti_nomor(numb)
                        break
                else:
                    print(f"MASUKKAN ANGKA SESUAI YG TERTERA")
                    continue
            else:
                print("MASUKKAN INPUT NUMBER")
                continue
            
    def ganti_nama(self,convert):
        inputUser = input("NAMA BARU : ")
        self.content[convert-1][1] = inputUser
        Liaison_list = []
        for item in self.content:
            Liaison_list.append(",".join(item))
        with open("kontak.txt",mode="w") as var:
            for item in Liaison_list:
                        var.write(item + "\n")
                        
                        
    def ganti_gmail(self,convert):
        inputUser = input("GMAIL BARU : ")
        self.content[convert-1][2] = inputUser
        Liaison_list = []
        for item in self.content:
            Liaison_list.append(",".join(item))
        with open("kontak.txt",mode="w") as var:
            for item in Liaison_list:
                        var.write(item + "\n")
                        
                        
    def ganti_nomor(self,convert):
        inputUser = input("NOMOR BARU : ")
        self.content[convert-1][3] = inputUser
        Liaison_list = []
        for item in self.content:
            Liaison_list.append(",".join(item))
        with open("kontak.txt",mode="w") as var:
            for item in Liaison_list:
                        var.write(item + "\n")
                        
                        
    def tambah_kontak(self):
        print("1. MENAMBAH KONTAK UMUM\n2. MENAMBAH KONTAK FAVORIT")
        while True:
            inputUser = input(">> ")
            if inputUser.isdigit():
                convert = int(inputUser)
                if convert == 1:
                    self.tambah_kontak_umum()
                    break
                elif convert == 2:
                    self.tambah_kontak_fav()
                    break
                else:
                    print("MASUKKAN ANGKA YG SESUAI")
                    continue
            else:
                print("MASUKKAN INPUT YG BENAR")
                continue
            
    def tambah_kontak_umum(self):
        Liaison_list = []
        Liaison_list.append("umum")
        inputUser = input("NAMA : ")
        Liaison_list.append(inputUser)
        inputUser = input("GMAIL : ")
        Liaison_list.append(inputUser)
        while True:
            inputUser = input("NOMOR : ")
            if inputUser.isdigit():
                Liaison_list.append(inputUser)
                break
            else:
                print("MASUKKAN NOMOR YG BENAR")
                continue
        with open("kontak.txt",mode="a") as var:
            item = ",".join(Liaison_list)
            var.write(item+"\n")
        print("TELAH DI TAMBAHKAN")
        
        
    def tambah_kontak_fav(self):
        changing_list = []
        changing_list.append("favorit")
        inputUser = input("NAMA : ")
        changing_list.append(inputUser)
        inputUser = input("GMAIL : ")
        changing_list.append(inputUser)
        while True:
            inputUser = input("NOMOR : ")
            if inputUser.isdigit():
                changing_list.append(inputUser)
                break
            else:
                print("MASUKKAN NOMOR YG BENAR")
                continue
        self.content.insert(0,changing_list)
        Liaison_list = []
        for item in self.content:
            Liaison_list.append(",".join(item))
        with open("kontak.txt",mode="w") as var:
            for item in Liaison_list:
                        var.write(item + "\n")
        print("TELAH DI TAMBAHKAN")
        
        
    def hapus_kontak(self):
        while True:
            inputUser = input("MASUKKAN INDEX KONTAK NOMOR BERAPA YG INGIN DI HAPUS\n>> ")
            if inputUser.isdigit():
                convert = int(inputUser)
                if convert > 0 and convert <= len(self.content):
                    del self.content[convert-1]
                    Liaison_list = []
                    for item in self.content:
                        Liaison_list.append(",".join(item))
                    with open("kontak.txt",mode="w") as var:
                        for item in Liaison_list:
                            var.write(item + "\n")
                    print("TELAH DI HAPUS")
                    break
                else:
                    print("MASUKKAN ANGKA SESUAI INDEX")
                    continue
            else:
                print("MASUKKAN ANGKA SESUAI INDEX")
                continue




menu = Menu()
while True :
    print(f"\n\n{" "*5} KONTAK")
    status = menu.tampilkan_semua_kontak()
    if status == 1:
        print("PILIHAN :\n1. Tambahkan kontak\n2. keluar")
        user_input = input(">> ")
        convert = int(user_input)
        if user_input.isdigit and convert <= 2 and convert != 0:
            if convert == 1 :
                menu.tambah_kontak()
                continue
            else :
                print("EXIT")
                break
        else :
            print("Masukkan index yang benar")
            continue
    else:
        print("PILIHAN :\n1. Tambahkan kontak\n2. Hapus kontak\n3. edit kontak\n4. keluar")
        user_input = input(">> ")
        convert = int(user_input)
        if user_input.isdigit and convert <= 4 and convert != 0:
            if convert == 1 :
                menu.tambah_kontak()
                continue
            elif convert == 2 :
                menu.hapus_kontak()
                continue
            elif convert == 3 :
                menu.edit_kontak()
                continue
            else :
                print("EXIT")
                break
        else :
            print("Masukkan index yang benar")
            continue
