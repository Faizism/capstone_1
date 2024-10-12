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
def read():
    print("Daftar Smartphone di Toko Berkah Jaya\n")
    print(f"{('id').ljust(10)}|{('Nama Smartphone').ljust(30)}|{('Harga').ljust(20)}|Stok")
    for item in product :
        print(f"{item['id'].ljust(10)}|{item['nama produk'].ljust(30)}|{str(item['harga']).ljust(20)}|{str(item['stok']).ljust(20)}")
    return

def create():
    """Function for create the data
    """
    return

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