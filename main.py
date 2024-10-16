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

def read():
    menu = input('''
    Menu 1 : Menampilkan Data Smartphone
    1. Menampilkan Seluruh Data Smartphone
    2. Mencari Data Smartphone Berdasarkan id
    3. Mencari Data Smartphone Berdasarkan Harga
    4. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
        display(product)
    elif menu == '2':
        try :
            id = input('Masukkan id Produk Smartphone yang ingin dilihat :').upper()
            if len(id) == 3 and id[0] == 'P' and id[1:].isdigit():
                filtered_id = [item for item in product if item['id']==id] 
                if filtered_id :
                    display(filtered_id)
                else :
                    print(f"Produk dengan id {id} tidak ditemukan")   
        except ValueError:
            print('Masukkan format id yang benar')

    # elif menu == '3':
    #     try:
    #         min_price = int(input("Masukkan harga minimum: "))
    #         max_price = int(input("Masukkan harga maksimum: "))
    #         filtered_product = [item for item in product if min_price <= item['harga']<= max_price]
    #         if filtered_product == []:
    #             print(f"Smartphone pada rentang harga {min_price} - {max_price} Tidak Tersedia")
    #         else:
    #             display(filtered_product)
    #     except ValueError:
    #         print('Masukkan Harga Yang Benar')
    elif menu == '4':
        main()
    else :
        print('Menu Tidak Tersedia')
    read()

def create():
    menu = input('''
    Menu 2 : Menambahkan Daftar Smartphone
    1. Menambah Data Smartphone Baru
    2. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
        add_id = input("Masukkan id Produk Smartphone Baru: ").upper()
        if len(add_id) == 3 and add_id[0] == 'P' and add_id[1:].isdigit():
            confirm_id = any(item['id']==add_id for item in product)
            if confirm_id :
                print("Data Sudah Ada")
                return create()
            else : 
                add_name = input("Masukkan Merk Smartphone & Serinya: ")
                while True:
                    try:  
                        add_price= int(input("Masukkan Harga per unit: "))
                        break
                    except ValueError:
                        print("Harga harus berupa angka. Silahkan coba lagi")
                while True:
                    try:
                        add_stock = int(input("Masukkan Stok: "))
                        break
                    except ValueError :
                        print("Stok Harus Berupa Angka. Silahkan Coba Lagi")
                new_id = f'P{int(product[-1]['id'][1:]) + 1 :02d}'

                while True:
                    confirm = input("Apakah Data akan disimpan? (Y/N): ").upper()
                    if confirm == 'Y':
                        product.append({'id':new_id,
                                        'nama produk':add_name,
                                        'harga': add_price,
                                        'stok': add_stock})
                        print("Data Smartphone Berhasil Ditambahkan")
                        break
                    elif confirm == 'N':
                        return create()
                    else:
                        False
    elif menu == '2':
        main()
    else:
        print("Menu Tidak Tersedia")
    create()

def edit(id) :
    index = next((index for (index, key) in enumerate(product) if key["id"] == id), None)   
    if index is not None :
        item = product[index]
        while True:
            confirmation = input(f"Apakah anda ingin mengubah data produk dengan id {item['id']} (Y/N): ").upper()
            if confirmation == 'Y' :
                while True :
                    menu_edit = input('''
                    Pilih kolom yang ingin diupdate
                    1. Nama Produk
                    2. Harga
                    3. Stok
                    4. Kembali ke Menu Edit
                    Masukkan angka kolom yang ingin diupdate :''')
                    if menu_edit == '1':
                        new_name = input("Masukkan Nama Produk: ")
                        while True:
                            confirm_name = input("Apakah Data akan diubah? (Y/N): ").upper()
                            if confirm_name == 'Y':
                                item['nama produk'] = new_name
                                print("Data Telah diubah")
                                update()
                            elif confirm_name == 'N':
                                update()
                            else:
                                False
                    elif menu_edit == '2':
                        while True:
                            new_price = input("Masukkan Harga Produk: ")
                            if new_price.isnumeric() :
                                while True:
                                    confirm_name = input("Apakah Data akan diubah? (Y/N): ").upper()
                                    if confirm_name == 'Y':
                                        item['harga'] = new_price
                                        print("Data Telah diubah")
                                        update()
                                    elif confirm_name == 'N':
                                        update()
                                    else:
                                        False
                            else :
                                print("Input Invalid. Masukkan Harga dalam Angka")
                    elif menu_edit == '3':
                        while True:
                            new_stock = input("Masukkan Stok Produk: ")
                            if new_stock.isnumeric() :
                                while True:
                                    confirm_name = input("Apakah Data akan diubah? (Y/N): ").upper()
                                    if confirm_name == 'Y':
                                        item['stok'] = new_stock
                                        print("Data Telah diubah")
                                        update()
                                    elif confirm_name == 'N':
                                        update()
                                    else:
                                        False
                            else :
                                print("Input Invalid. Masukkan Stok dalam Angka ")
                    elif menu_edit == '4':
                        update()
                    else :
                        print("Input Tidak Valid")
            elif confirmation == 'N':
                return update()
            else :
                print("Input tidak valid. Mohon masukkan 'Y' atau 'N'.")

def update():
    menu = input('''
    Menu 3 : Ubah Data Smartphone
    1. Ubah Data Smartphone
    2. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
        try:
            id = input('Masukkan id Produk Smartphone yang ingin diubah :').upper()
            if len(id) == 3 and id[0] == 'P' and id[1:].isdigit():
                filtered_id = [item for item in product if item['id']==id]
                display(filtered_id)
                edit(id)
            else :
                print("Data Produk yang Anda Cari Tidak Ada")
        except ValueError:
            print('Masukkan id yang Benar')

    elif menu == '2':
        main()
    else:
        print("Menu Tidak Tersedia")
        main()

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    print("""Database Penjualan Toko Smartphone Berkah Jaya
    Pilih menu yang ingin di jalankan
    1. Lihat Daftar Smartphone
    2. Tambah Smartphone Baru
    3. Ubah Data Smartphone
    4. Hapus Smartphone dari Dafar
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
