# TPM
#
member = input("Apakah Member? : ")
total_belanja = float(input("masukkan total belanja = Rp. "))


if member == 'ya' and total_belanja > 500.000:
    diskon_persen = 20
elif member == 'ya' and total_belanja <= 500.000:
    diskon_persen = 10 
elif member == 'tidak' and total_belanja > 500.000:
    diskon_persen = 5
elif member == 'tidak' and total_belanja <= 500.000:
    diskon_persen = 0

diskon_Rp = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - diskon_Rp

print(f"total Belanja: Rp. {total_belanja:.03f}")
print(f"diskon_persen: {diskon_persen}%")
print(f"diskon Rp: Rp. {diskon_Rp:.03f}")
print(f"bayar Rp: {total_bayar:.03f}")

   