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
def display():
    print("Daftar Smartphone di Toko Berkah Jaya\n")
    print(f"{('id').ljust(10)}|{('Nama Smartphone').ljust(30)}|{('Harga').ljust(20)}|Stok")
    for item in product :
        print(f"{item['id'].ljust(10)}|{item['nama produk'].ljust(30)}|{str(item['harga']).ljust(20)}|{str(item['stok']).ljust(20)}")

def read():
    menu = input('''
    Menu 1 : Menampilkan Data Smartphone
    1. Menampilkan Seluruh Data Smartphone
    2. Mencari Data HP Berdasarkan Harga
    3. Kembali ke Menu Awal
    Masukkan angka Menu yang ingin di jalankan: ''')
    if menu == '1':
        display()
    elif menu == '2':
        try:
            min_price = int(input("Masukkan harga minimum: "))
            max_price = int(input("Masukkan harga maksimum: "))
            filtered_product = [item for item in product if min_price <= item['harga']<= max_price]
            if filtered_product == []:
                print(f"Smartphone pada rentang harga {min_price} - {max_price} Tidak Tersedia")
            else:
                print(filtered_product)
        except ValueError:
            print('Masukkan Harga Yang Benar')
    elif menu == '3':
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
        add_name = input("Masukkan Merk Smartphone & Serinya: ")
        add_price= input("Masukkan Harga per unit: ")
        add_stock = input("Masukkan Stok: ")
        new_id = f'P{int(product[-1]['id'][1:]) + 1 :02d}'
        product.append({
            'id':new_id,
            'nama produk':add_name,
            'harga': add_price,
            'stok': add_stock
        })
        print("Data Smartphone Berhasil Ditambahkan")
        display()

def update():
    """Function for update the data
    """
    return

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
    else:
        print("Input is not valid !")


if __name__ == "__main__":
    main()

main()