# meminta input dari pengguna dalam fahrenheit 
fahrenheit = float (input("masukkan temperatur dalam fahrenheit :")) 

# mengonfersi fahrenheit ke celcius 
celcius = (fahrenheit - 32 ) * 5/9 

# menampilkan hasil konvensi 
print (f"{fahrenheit} derajat fahreheit = {celcius :.2f} derajat celcius") 