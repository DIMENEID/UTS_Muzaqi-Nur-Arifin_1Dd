#VARIABEL GLOBAL  --> variabel yang bisa dipanggil ke beberapa function (variabel tidak terikat)
name = 'Muzaqi Nur Arifin'

def cetak_name1():
    print(f'Nama saya adalah : {name}')
    
def cetak_name2():
    print(f'Nama saya adalah : {name}')
    
cetak_name1()
cetak_name2()



# VARIABEL LOKAL
def cetak_name1():
    name = 'Muzaqi'
    print(f'Nama saya adalah : {name}')
    
def cetak_name2():
    name = 'Fakhri'
    print(f'Nama saya adalah : {name}')
    
cetak_name1()
cetak_name2()

    
    