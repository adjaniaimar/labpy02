# Kalkulator Sederhana
while True:
    angka1 = float(input("Masukan angka 1:"))
    operator = input("Masukan operator(+,-,*,/):")
    angka2 = float(input("Masukan angka 2:"))

    if operator == '+':
        hasil = angka1+angka2
    elif operator == '-':
        hasil = angka1-angka2
    elif operator == '*':
        hasil = angka1*angka2
    elif operator == '/':
        hasil = angka1/angka2
    
    print("Hasil nya adalah:", hasil)

# Tanyakah apakah ingin lanjut?
    lagi = input("Apakah ingin coba lagi?(ya/tidak):")

    if lagi != 'ya':
        print("Terimakasih sudah mencoba kalkulator sederhana by Nevillaz")
        break