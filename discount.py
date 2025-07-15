barang = input('input nama barang: ')
harga = int(input('input harganya : '))

if harga >= 250000:
  harga_awal = harga
  diskon = 20
  harga_akhir = harga_awal - (harga_awal * diskon / 100)
  print(f'Barang : {barang}')
  print(f'Diskon : 20%')
  print(f'Harga Akhir : Rp.{int(harga_akhir)}')
  print('Wah!! Kamu Hemat Banget🤑')
elif harga >= 150000: 
  harga_awal = harga
  diskon = 10
  harga_akhir = harga_awal - (harga_awal * diskon / 100)
  print(f'Barang : {barang}')
  print(f'Diskon : 10%')
  print(f'Harga Akhir : Rp.{int(harga_akhir)}')
  print('Wah!! Kamu Hemat Banget🤑')
else:
  print(f'Barang : {barang}')
  print(f'Diskon : ???')
  print(f'Harga Akhir : Rp.{int(harga)}')
  print('Ayo! berbelanja diatas 150.000 agar mendapatkan diskon hingga 20%🤑🤑')