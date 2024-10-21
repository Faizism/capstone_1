# ===================================
# Database Penjualan Smartphone
# ===================================
# Developed by. Muhammad Fa'iz Ismail
# JCDS - 0412


# /************************************/

# /===== Data Model =====/
# Create your data model here

product = [{'id' : 'P01',  'nama produk' : 'Redmi 12', 'harga': 2_000_000, 'stok' : 12},
{'id' : 'P02', 'nama produk' : 'Samsung Galaxy A34 5G', 'harga':4_500_000, 'stok' : 18 },
{'id' : 'P03', 'nama produk' : 'Google Pixel 7a', 'harga':6_000_000, 'stok' : 8 },
{'id' : 'P04', 'nama produk' : 'iPhone 14', 'harga':14_000_000, 'stok' : 10 },
{'id' : 'P05', 'nama produk' : 'Samsung Galaxy S23 Ultra', 'harga':20_000_000, 'stok' : 15 }]

# /===== Feature Program =====/
# Create your feature program here
def display(items):
    """ Menampilkan daftar smartphone yang tersedia di toko.

    Args:
        items (list): Daftar dictionary yang berisi informasi smartphone.
                      Setiap dictionary berisi:
                      - 'id': string (id produk)
                      - 'nama produk': string (nama smartphone)
                      - 'harga': int atau float (harga smartphone)
                      - 'stok': int (jumlah stok tersedia)
    """
    print("Daftar Smartphone di Toko Berkah Jaya\n")
    print(f"{('id').ljust(10)}|{('Nama Smartphone').ljust(30)}|{('Harga').ljust(20)}|Stok")
    for item in items :
        print(f"{item['id'].ljust(10)}|{item['nama produk'].ljust(30)}|{str(item['harga']).ljust(20)}|{str(item['stok'])}")

def get_valid_input(prompt, validator, error_msg):
    """ Meminta input dari pengguna hingga input tersebut valid.

    Args:
        prompt (str): Pesan yang ditampilkan untuk meminta input dari pengguna.
        validator (function): Fungsi yang menerima input dan mengembalikan True jika input valid, False jika tidak.
        error_msg (str): Pesan error yang ditampilkan jika input tidak valid

    Returns:
        str : Input pengguna yang valid setelah lolos pengecekan oleh
    """
    while True:
        user_input = input(prompt).upper()
        if validator(user_input):
            return user_input
        print(error_msg)

def validator_id(id_str):
    """ Memvalidasi apakah string id sesuai dengan format yang diharapkan.

    Args:
        id_str (str): String yang merepresentasikan id untuk divalidasi

    Returns:
        bool: True jika id valid (panjangnya 3, dimulai dengan 'P', dan diikuti oleh angka), 
              False jika tidak.
    """
    return len(id_str) == 3 and id_str[0] == 'P' and id_str[1:].isdigit()

def get_product_by_id(id_str, product_list):
    """ Mendapatkat item dari produk berdasarkan ID dari daftar produk.

    Args:
        id_str (str): ID produk yang akan dicari.
        product_list (list): Daftar produk, di mana setiap produk berupa dictionary
                             dengan kunci "id" dan informasi lainnya

    Returns:
        dict or None: Dictionary berisi data produk jika ID ditemukan, 
                      atau None jika tidak ada produk dengan ID yang sesuai.
    """
    return next((item for item in product_list if item["id"] == id_str), None)

def validator_price(price_str):
    """ Memvalidasi apakah string price sesuai dengan format yang diharapkan

    Args:
        price_str (str): String yang merepresentasikan price untuk divalidasi

    Returns:
        bool: True jika price valid (input berupa digit angka, panjangnya lebih dari sama dengan 5, dan berupa bilangan positif), 
              False jika tidak.
    """
    return price_str.isdigit() and len(price_str)>=5 and int(price_str)>0

def validator_stock(stock_str):
    """ Memvalidasi apakah string stock sesuai dengan format yang diharapkan

    Args:
        stock_str (str): String yang merepresentasikan stock untuk divalidasi

    Returns:
        bool: True jika stock valid (input berupa digit angka, dan berupa bilangan positif), 
              False jika tidak.
    """
    return stock_str.isdigit() and int(stock_str)>0

def get_confirmation(prompt):
    """ Meminta konfirmasi dari pengguna dalam bentuk input Y atau N.

    Args:
        prompt (str): Pesan yang ditampilkan untuk meminta konfirmasi dari pengguna.

    Returns:
        bool: True jika pengguna mengonfirmasi dengan 'Y', False jika pengguna menolak dengan 'N'.
    """
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
    """ 
    Menampilkan menu untuk membaca data smartphone dari daftar produk.

    Berdasarkan input pengguna, fungsi ini menjalankan opsi yang sesuai:
    - Jika memilih opsi 1, seluruh data smartphone akan ditampilkan.
    - Jika memilih opsi 2, pengguna diminta memasukkan ID, lalu mencari dan menampilkan data smartphone dengan ID tersebut.
    - Jika memilih opsi 3, fungsi akan kembali ke menu awal.
    - Jika input tidak valid, fungsi menampilkan pesan kesalahan.

    Fungsi ini berjalan dalam loop hingga pengguna memilih untuk kembali ke menu awal.

    """
    while True:
        menu = input('''
            Menu 1 : Menampilkan Data Smartphone
            1. Menampilkan Seluruh Data Smartphone
            2. Mencari Data Smartphone Berdasarkan ID
            3. Mencari Data Smartphone Berdasarkan Nama Merk
            4. Mencari Data Smartphone Berdasarkan Harga
            5. Kembali ke Menu Awal
            Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            display(product)
        elif menu == '2':
            id_read = get_valid_input('Masukkan id Produk Smartphone yang ingin ditampilkan: ',
                                        validator_id,"Format ID Tidak Valid")
            item = get_product_by_id(id_read, product)
            if item:
                display([item])
            else:
                print(f"Produk dengan ID {id_read} tidak ditemukan")
        elif menu == '3':
            name_read = input("Masukkan Merk Smartphone yang Ingin dicari: ")
            filter_name = [item for item in product if item["nama produk"].split()[0].lower() == name_read.lower()]
            if filter_name == [] :
                print(f"Smartphone dengan merk {name_read} Tidak Tersedia")
            else :
                print(f"Berikut produk dengan Merk {name_read}: ")
                display(filter_name)
        elif menu == '4':
            price_read_min = get_valid_input('Masukkan Harga Minimum Smartphone yang ingin dicari: ',
                                            validator_price,"Format Harga Tidak Sesuai")
            price_read_max = get_valid_input('Masukkan Harga Maksimum Smartphone yang ingin dicari: ',
                                            validator_price,"Format Harga Tidak Sesuai")
            filter_price = [item for item in product if int(price_read_min) <= item['harga']<= int(price_read_max)]
            if filter_price == []:
                print(f"Smartphone pada rentang harga {price_read_min} - {price_read_max} Tidak Tersedia")
            else :
                print(f"Berikut Smartphone pada rentang harga {price_read_min} - {price_read_max}")
                display(filter_price)
        elif menu == '5':
            break
        else :
            print('Menu Tidak Tersedia')

def create():
    """
    Menampilkan menu untuk menambahkan data smartphone ke dalam daftar produk.

    Alur fungsi:
    - Jika memilih opsi 1, pengguna akan diminta untuk memasukkan ID produk, nama, harga, dan stok. 
      Sebelum data ditambahkan, fungsi memeriksa apakah ID yang dimasukkan sudah ada di daftar produk.
      Jika ID sudah ada, maka pengguna akan diberitahu bahwa data sudah ada.
    - Jika ID belum ada, fungsi akan menambahkan data baru berdasarkan input pengguna.
    - Pengguna akan diminta konfirmasi sebelum data disimpan.
    - Jika memilih opsi 2, fungsi akan kembali ke menu awal.
    - Jika input tidak valid, fungsi menampilkan pesan kesalahan.
    """
    while True:
        menu = input('''
        Menu 2 : Menambahkan Daftar Smartphone
        1. Menambah Data Smartphone Baru
        2. Kembali ke Menu Awal
        Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            id_create = get_valid_input ('Masukkan id Produk yang ingin ditambah: ',
                                        validator_id, "Format ID Tidak Valid")
            item = get_product_by_id(id_create, product)
            if item:
                print("Data Sudah Ada")
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
        elif menu == '2':
            break
        else:
            print("Menu Tidak Tersedia")

def update():
    """
    Menampilkan menu untuk memperbarui data smartphone berdasarkan ID.

    Alur fungsi:
    1. Pengguna diminta untuk memasukkan ID produk.
    2. Jika produk ditemukan, data ditampilkan dan pengguna dapat memilih kategori (nama produk, harga, atau stok) yang ingin diubah.
    3. Setelah pengguna mengonfirmasi perubahan, data akan diperbarui dengan nilai baru.
    4. Jika input kategori atau ID tidak valid, pengguna akan diberi pesan kesalahan dan diminta input ulang.

    """
    while True :
        menu = input('''
        Menu 3 : Ubah Data Smartphone
        1. Ubah Data Smartphone Berdasarkan id
        2. Kembali ke Menu Awal
        Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            id_update = get_valid_input('Masukkan id Produk yang ingin diubah: ', validator_id, "Format ID Tidak Valid")
            item = get_product_by_id(id_update, product)
            if item:
                display([item])
                if get_confirmation("Apakah Data akan diubah? (Y/N): "):
                    category = input("Pilih field yang ingin diubah (nama produk/harga/stok): ").lower()
                    if category in ['nama produk', 'harga', 'stok']:
                        if category == 'nama produk':
                            new_value = input(f"Masukkan {category} baru: ")
                        elif category == 'harga':
                            new_value = get_valid_input(f"Masukkan {category} baru: ", validator_price, 
                                                        "Harga harus berupa angka positif dan lebih dari 5 digit")
                        elif category == 'stok':
                            new_value = get_valid_input(f"Masukkan {category} baru: ", validator_stock, 
                                                        "Stok harus berupa angka non-negatif")
                        if get_confirmation("Apakah Data akan diubah? (Y/N): "):
                            if category == 'nama produk':
                                item['nama produk'] = new_value
                            elif category == 'harga':
                                item['harga'] = int(new_value)
                            else:
                                item['stok'] = int(new_value)
                            print("Data berhasil diubah")
                    else:
                        print("Kategori tidak valid")
            else:
                print(f"Produk dengan id {id_update} tidak ditemukan")
        elif menu == '2':
            break
        else:
            print("Menu Tidak Tersedia")

def delete():
    """
    Menampilkan menu untuk menghapus data smartphone dari daftar produk berdasarkan ID.

    Alur fungsi:
    1. Pengguna diminta untuk memasukkan ID produk.
    2. Jika produk ditemukan, data produk ditampilkan dan pengguna diminta konfirmasi sebelum penghapusan.
    3. Jika penghapusan dikonfirmasi, data produk akan dihapus dari daftar.
    4. Jika ID tidak valid atau produk tidak ditemukan, pengguna diberi pesan kesalahan.

    """
    while True :
        menu = input ('''
        Menu 4 : Hapus Smartphone dari Daftar
        1. Hapus Smartphone Berdasarkan id
        2. Kembali ke Menu Awal
        Masukkan angka Menu yang ingin di jalankan: ''')
        if menu == '1':
            display(product)
            id_delete = get_valid_input ('Masukkan id Produk yang ingin dihapus: ',
                                            validator_id, "Format ID Tidak Valid")
            item = get_product_by_id(id_delete, product)

            if item:
                display ([item])
                if get_confirmation("Apakah Data akan dihapus? (Y/N): ") :
                    product.remove(item)
                    print("Data Telah Dihapus")
            else:
                print(f"Pduk dengan ID {id_delete} tidak ditemukan")
        elif menu == '2':
            break
        else:
            print("Menu Tidak Tersedia")

def sorting():
    while True :
        menu = input('''
        Menu 5: Urutan Smartphone
        1. Sortir daftar produk berdasarkan harga
        2. Sortir daftar produk berdasarkan stok
        3. Sortir daftar produk berdasarkan nama
        4. Kembali ke menu awal
        Masukkan angka Menu yang ingin dijalankan: ''')
        if menu == '1' :
            while True :
                menu_sort_price = input('''
                1. Sortir Smartphone dari termurah
                2. Sortir Smartphone dari termahal
                3. Kembali ke menu sortir
                Masukkan angka Menu yang ingin dijalankan: ''')
                if menu_sort_price == '1':
                    display(sorted(product, key=lambda x : x['harga']))
                elif menu_sort_price == '2' :
                    display(sorted(product, key=lambda x : -x['harga']))
                elif menu_sort_price == '3':
                    break
                else :
                    print("Menu Tidak Tersedia")
        elif menu == '2' :
            while True :
                menu_sort_stock = input('''
                1. Sortir Smartphone dari stok terkecil
                2. Sortir Smartphone dari stok terbesar
                3. Kembali ke menu sortir
                Masukkan angka Menu yang ingin dijalankan: ''')
                if menu_sort_stock == '1':
                    display(sorted(product, key=lambda x : x['stok']))
                elif menu_sort_stock == '2' :
                    display(sorted(product, key=lambda x : -x['stok']))
                elif menu_sort_stock == '3':
                    break
                else :
                    print("Menu Tidak Tersedia")
        elif menu == '3' :
            while True :
                menu_sort_name = input('''
                1. Sortir Smartphone dari A-Z
                2. Sortir Smartphone dari Z-A
                3. Kembali ke menu sortir
                Masukkan angka Menu yang ingin dijalankan: ''')
                if menu_sort_name == '1':
                    display(sorted(product, key=lambda x : x['nama produk']))
                elif menu_sort_name == '2' :
                    display(sorted(product, key=lambda x : -x['nama produk']))
                elif menu_sort_name == '3':
                    break
                else :
                    print("Menu Tidak Tersedia")
        elif menu == '4':
            break
        else :
            print("Menu Tidak Tersedia")
        

# /===== Main Program =====/
# Create your main program here
def main():
    """
    Program utama untuk mengelola database penjualan Toko Smartphone Berkah Jaya.

    Berdasarkan input pengguna, fungsi akan menjalankan tindakan yang sesuai dengan memanggil fungsi `read()`, `create()`, `update()`, atau `delete()`.
    Jika pengguna memilih untuk keluar, program akan menampilkan pesan perpisahan dan berhenti.
    Jika input tidak valid, pengguna akan diminta untuk menginput ulang hingga pilihan yang valid dimasukkan.

    """
    while True :
        print("""Database Penjualan Toko Smartphone Berkah Jaya
        Pilih menu yang ingin di jalankan
        1. Lihat Daftar Smartphone
        2. Tambah Smartphone Baru
        3. Ubah Data Smartphone
        4. Hapus Smartphone dari Daftar
        5. Sortir Daftar Produk
        6. Keluar dari Program
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
            sorting()
        elif input_user == "6":
            print("Thank You and Goodbye")
            break
        else:
            print("Input is not valid")


if __name__ == "__main__":
    main()