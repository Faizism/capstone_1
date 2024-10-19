# ===================================
# Database Penjualan Smartphone
# ===================================
# Developed by. Muhammad Fa'iz Ismail
# JCDS - 0412


# /************************************/

# /===== Data Model =====/
# Create your data model here

product = [{'id' : 'P01', 'nama produk' : 'Redmi 12', 'harga': 2_000_000, 'stok' : 12},
{'id' : 'P02', 'nama produk' : 'Samsung Galaxy A34 5G', 'harga':4_500_000, 'stok' : 18 },
{'id' : 'P03', 'nama produk' : 'Google Pixel 7a', 'harga':6_000_000, 'stok' : 8 },
{'id' : 'P04', 'nama produk' : 'iPhone 14', 'harga':14_000_000, 'stok' : 10 },
{'id' : 'P05', 'nama produk' : 'Samsung Galaxy S23 Ultra', 'harga':20_000_000, 'stok' : 15 }]

# /===== Feature Program =====/
# Create your feature program here
def display(items):
    print("Daftar Smartphone di Toko Berkah Jaya\n")
    print(f"{('id').ljust(10)}|{('Nama Smartphone').ljust(30)}|{('Harga').ljust(20)}|Stok")
    for item in items :
        print(f"{item['id'].ljust(10)}|{item['nama produk'].ljust(30)}|{str(item['harga']).ljust(20)}|{str(item['stok'])}")

def get_valid_input(prompt, validator, error_msg):
    while True:
        user_input = input(prompt).upper()
        if validator(user_input):
            return user_input
        print(error_msg)

def validator_id(id_str):
    return len(id_str) == 3 and id_str[0] == 'P' and id_str[1:].isdigit()

def get_product_by_id(id_str, product_list):
    return next((item for item in product_list if item["id"] == id_str), None)

def validator_price(price_str):
    return price_str.isdigit() and len(price_str)>=5 and int(price_str)>0

def validator_stock(stock_str):
    return stock_str.isdigit() and int(stock_str)>0

def get_confirmation(prompt):
    while True:
        confirm = input(prompt).upper()
        if confirm == 'Y':
            return True
        elif confirm == 'N':
            print("Data Tidak Tersimpan")
            return False
        else:
            print("Input tidak valid. Masukkan Y atau N ")

def read():
    while True:
        menu = input('''
        Menu 1 : Menampilkan Data Smartphone
        1. Menampilkan Seluruh Data Smartphone
        2. Mencari Data Smartphone Berdasarkan id
        3. Kembali ke Menu Awal
        Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            display(product)
        elif menu == '2':
            id_read = get_valid_input('Masukkan id Produk Smartphone yang ingin ditampilkan: ',
                                    validator_id,"Format ID Tidak Valid")
            item = get_product_by_id(id_read, product)
            if item:
                display([item])
                read()
            else:
                print(f"Produk dengan ID {id_read} tidak ditemukan")
                read()
        elif menu == '3':
            main()
        else :
            print('Menu Tidak Tersedia')

def create():
    menu = input('''
    Menu 2 : Menambahkan Daftar Smartphone
    1. Menambah Data Smartphone Baru
    2. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
        while True:
            id_create = get_valid_input ('Masukkan id Produk yang ingin ditambah: ',
                                         validator_id, "Format ID Tidak Valid")
            item = get_product_by_id(id_create, product)
            if item:
                print("Data Sudah Ada")
                create()
            else :
                new_id = f'P{int(product[-1]["id"][1:]) + 1:02d}'
                add_name = input("Masukkan Merk Smartphone & Serinya: ")
                add_price = int(get_valid_input("Masukkan Harga per unit: ",validator_price, "Harga harus berupa angka positif dan lebih dari 5 digit"))
                add_stock = int(get_valid_input("Masukkan Stok: ", validator_stock, "Stok harus berupa angka non-negatif"))

                if get_confirmation ("Apakah Data akan disimpan? (Y/N): ") :
                    product.append({'id':new_id,
                                    'nama produk':add_name,
                                    'harga': add_price,
                                    'stok': add_stock})
                    print("Data Smartphone Berhasil Ditambahkan")
                    create()
                else :
                    create()
    elif menu == '2':
        main()
    else:
        print("Menu Tidak Tersedia")

def update():
    while True:
        menu = input('''
        Menu 3 : Ubah Data Smartphone
        1. Ubah Data Smartphone Bds id
        2. Kembali ke Menu Awal
        Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            id_update = get_valid_input ('Masukkan id Produk yang ingin diubah: ',
                                         validator_id, "Format ID Tidak Valid")
            item = get_product_by_id(id_update, product)
            if item:
                display([item])

                category = input("Pilih field yang ingin diubah (nama produk/harga/stok): ").lower()
                if category in ['nama produk', 'harga', 'stok'] :
                    if category == 'nama produk':
                        new_value = input(f"Masukkan {category} baru: ")
                    if category == 'harga':
                        new_value = get_valid_input(f"Masukkan {category} baru: ", validator_price, 
                                                    "Harga harus berupa angka positif dan lebih dari 5 digit")
                    elif category == 'stok':
                        new_value = get_valid_input(f"Masukkan {category} baru: ", validator_stock, 
                                                    "Stok harus berupa angka non-negatif")
                    if get_confirmation("Apakah Data akan diubah? (Y/N): ") :
                        if category == 'nama produk':
                            item['nama produk'] = new_value
                        elif category == 'harga':
                            item['harga'] = int(new_value)
                        else:
                            item['stok'] = int(new_value)
                        print("Data berhasil diubah")
                else :
                    print("Kategori tidak valid")
                    update()
            else :
                print(f"Produk dengan id {id_update} tidak ditemukan")
                update()

        elif menu == '2':
            main()
        else:
            print("Menu Tidak Tersedia")
            main()   

def delete():
    menu = input ('''
    Menu 4 : Hapus Smartphone dari Daftar
    1. Hapus Smartphone Bds id
    2. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
            id_del = input('Masukkan id Produk Smartphone yang ingin dihapus: ').upper()
            if len(id_del) == 3 and id_del[0] == 'P' and id_del[1:].isdigit():
                index = next((index for (index, d) in enumerate(product) if d["id"] == id_del), None)
                if index is not None:
                    item = product[index]
                    display([item])
                    while True :
                        confirm = input(f"Apakah Anda yakin ingin menghapus produk dengan ID {id_del}? (Y/N): ")
                        if confirm.upper() == 'Y':
                            del product[index]
                            print(f"Produk dengan ID {id_del} telah dihapus.")
                            delete()
                        elif confirm.upper() == 'N':
                            delete()
                        else :
                            print("Input tidak valid. Masukkan Y atau N.")
                            False
                else :
                    print(f"Produk dengan ID {id_del} tidak ditemukan")
            else :
                print("Format ID tidak valid")
    elif menu == '2':
        main()
    else:
        print("Menu Tidak Tersedia")
        delete()


# /===== Main Program =====/
# Create your main program here
def main():
    print("""Database Penjualan Toko Smartphone Berkah Jaya
    Pilih menu yang ingin di jalankan
    1. Lihat Daftar Smartphone
    2. Tambah Smartphone Baru
    3. Ubah Data Smartphone
    4. Hapus Smartphone dari Daftar
    5. Keluar dari Program
    """)

    input_user = input("Masukkan angka Menu yang ingin dijalankan: ")
    if input_user == "1":
        read()
    elif input_user == "2":
        create()
    elif input_user == "3":
        update()
    elif input_user == "4":
        delete()
    elif input_user == "5":
        print("Thank You and Goodbye")
    else:
        print("Input is not valid !")
        main()


if __name__ == "__main__":
    main()