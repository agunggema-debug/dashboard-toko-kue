import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_cake_data(rows=1000):
    start_date = datetime(2023, 1, 1)
    
    # Daftar produk dan harga
    products = {
        'Lapis Legit': {'cat': 'Kue Basah', 'price': 55000},
        'Brownies': {'cat': 'Kue Kering', 'price': 75000},
        'Croissant': {'cat': 'Pastry', 'price': 25000},
        'Donut': {'cat': 'Roti', 'price': 12000},
        'Cheese Cake': {'cat': 'Cake', 'price': 45000},
        'Bika Ambon': {'cat': 'Kue Basah', 'price': 40000},
        'Macaron': {'cat': 'Kue Kering', 'price': 15000}
    }
    
    product_names = list(products.keys())
    
    data = []
    for i in range(rows):
        # Pilih tanggal acak dalam 1 tahun
        date = start_date + timedelta(days=random.randint(0, 364))
        
        # Pilih produk
        prod = random.choice(product_names)
        category = products[prod]['cat']
        price_each = products[prod]['price']
        
        # Tentukan jumlah beli (1-10)
        quantity = random.randint(1, 10)
        total_sales = price_each * quantity
        
        data.append([date, prod, category, quantity, price_each, total_sales])
    
    # Buat DataFrame
    df = pd.DataFrame(data, columns=['Tanggal', 'Produk', 'Kategori', 'Jumlah', 'Harga_Satuan', 'Total_Penjualan'])
    
    # Urutkan berdasarkan tanggal
    df = df.sort_values(by='Tanggal')
    
    # Simpan ke CSV
    df.to_csv('retail_toko_kue.csv', index=False)
    print(f"Berhasil membuat {rows} data transaksi di 'retail_toko_kue.csv'")

if __name__ == "__main__":
    generate_cake_data(2000) # Membuat 2000 baris dataimport pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_cake_data(rows=1000):
    start_date = datetime(2023, 1, 1)
    
    # Daftar produk dan harga
    products = {
        'Lapis Legit': {'cat': 'Kue Basah', 'price': 55000},
        'Brownies': {'cat': 'Kue Kering', 'price': 75000},
        'Croissant': {'cat': 'Pastry', 'price': 25000},
        'Donut': {'cat': 'Roti', 'price': 12000},
        'Cheese Cake': {'cat': 'Cake', 'price': 45000},
        'Bika Ambon': {'cat': 'Kue Basah', 'price': 40000},
        'Macaron': {'cat': 'Kue Kering', 'price': 15000}
    }
    
    product_names = list(products.keys())
    
    data = []
    for i in range(rows):
        # Pilih tanggal acak dalam 1 tahun
        date = start_date + timedelta(days=random.randint(0, 364))
        
        # Pilih produk
        prod = random.choice(product_names)
        category = products[prod]['cat']
        price_each = products[prod]['price']
        
        # Tentukan jumlah beli (1-10)
        quantity = random.randint(1, 10)
        total_sales = price_each * quantity
        
        data.append([date, prod, category, quantity, price_each, total_sales])
    
    # Buat DataFrame
    df = pd.DataFrame(data, columns=['Tanggal', 'Produk', 'Kategori', 'Jumlah', 'Harga_Satuan', 'Total_Penjualan'])
    
    # Urutkan berdasarkan tanggal
    df = df.sort_values(by='Tanggal')
    
    # Simpan ke CSV
    df.to_csv('retail_toko_kue.csv', index=False)
    print(f"Berhasil membuat {rows} data transaksi di 'retail_toko_kue.csv'")

if __name__ == "__main__":
    generate_cake_data(2000) # Membuat 2000 baris data