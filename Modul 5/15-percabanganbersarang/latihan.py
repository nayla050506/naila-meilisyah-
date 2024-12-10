# Latihan 
# data data nilai

print(20*"=")
print("Data Nilai")
print(20*"=")

nilai = float(input("Masukkan Bilangan = "))
operator = input ("operator (>,<=, <=)")


# data nilai percabangannya

if operator == '>' : 
    hasil = nilai > 90 
    print ("nilai nilai huruf = A")
elif operator == '<=' : 
    hasil = nilai <= 90 and nilai >= 85 
    print ("hasl nilai huruf = A-")
elif operator == '<=' :
    hasil = nilai <= 85 and nilai >= 80
    print ("hasil nilai huruf = B+")
elif operator == '<=':
    hasil = nilai <= 79 and nilai >= 75 
    print ("hasil nilai huruf = B")
elif operator == '<=' : 
    hasil = nilai <= 74 and nilai >= 70 
    print ("hasil nilai huruf = B-")
elif operator == '<=' :
    hasil = nilai <= 69 and nilai >= 65 
    print ("hasil nilai huruf = c+")
elif operator == '<=' :
    hasil = nilai '<=' :
    print ("hasil nilai huruf = D")
elif operator == '<=' :
    hasil = nilai <= 59 and nilai >= 55
    print ("hasil nilai huruf = D")
elif operator == '<=' : 
    hasil = nilai < 55
    print ("hasil nilai huru = E")