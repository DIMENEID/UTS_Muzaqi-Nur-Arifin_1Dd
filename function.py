# function tanpa parameter -> function tanpa input

#FORMAT
# #def vaariabel():
#     condition

def cetak_string():
    print('hello world')
    
cetak_string()


# function dengan parameter -> function dengan inputan
def hello(name):
    print(f'Nama : {name}')

hello('Muzaqi Nur Arifin')


def luas_persegi_panjang(panjang,lebar):
    hasil = panjang*lebar
    print (f'Hasil Luas Persegi Panjang : {hasil} cm2')

luas_persegi_panjang(9,90)


def check_bilangan(nilai):
    if nilai % 2 == 0:
        print (f'Nilai : {nilai} adalah bilangan genap')
    else:
        print (f'Nilai : {nilai} adalah bilangan genap')
        
check_bilangan(10987898976765775677689078967654563535435434664243623421231432121342123426426424354646567576786786789787897090097878675)
#check_bilangan(int(input(f'')))                  #inputan pada function
        
def luas_persegi(sisi):
    hasil = sisi*sisi
    print (f'Luas Persegi : {hasil} cm2')

luas_persegi(int(input(f'Masukkan sisi :')))


#return
def cetak_integer(a):
    return a

print(cetak_integer(1))



