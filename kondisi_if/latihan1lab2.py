a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

if a >= b and a >= c and a >= d:
    terbesar = a
elif b >= a and b >= c and b >= d:
    terbesar = b
elif c >= a and c >= b and c >= d:
    terbesar = c
else:
    terbesar = d
    
print("Bilangan terbesar adalah:", terbesar)
