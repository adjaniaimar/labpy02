# Order Tiket Bioskop
reg = 50000
vip = 100000
order = input ("Tiket apa yang Anda ingin pesan?(Reguler/VIP): ")

if order == 'Reguler':
    ticket = reg
else:
    ticket = vip

disc = 0.8
member = input ("Apakah Anda mempunyai member?(Ya/Tidak): ")
if member == 'Ya':
    price = ticket * disc
else:
    price = ticket

qty = int(input("Berapa tiket yang Anda ingin beli?: "))
harga_akhir = price * qty
print("Anda membayar sebesar:", harga_akhir)