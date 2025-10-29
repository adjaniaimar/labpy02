a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

data = [a, b, c, d]

data.sort()

print("Data setelah diurutkan dari terkecil ke terbesar:")
for x in data:
    print(x, end=" ")
