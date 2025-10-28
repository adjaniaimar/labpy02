Nama = input("Nasukan nama Anda:")
UTS = input("Masukan nilai UTS:")
UAS = input("Masukan nilai UAS:")
Tugas = input("Masukan nilai Tugas:")

akhir = (int(Tugas) * .2) + (int(UTS) * .4) + (int(UAS) * .4)
keterangan = ("TIDAK LULUS", "LULUS") [akhir > 60.0]
if akhir > 80 :
    huruf = "A"
elif akhir > 70 :
    huruf = "B"
elif akhir > 50 :
    huruf = "C"
elif akhir > 40 :
    huruf = "D"
else:
    huruf = "E"

print("Nama         :",Nama)
print("Nilai UTS    :",UTS)
print("Nilai UAS    :",UAS)
print("Nilai Tugas  :",Tugas)
print("Nilai Akhir  :",akhir)
print("Nilai Huruf  :",huruf)
print("KETERANGAN   :",keterangan)