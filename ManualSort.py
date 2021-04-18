# Membuat Input untuk memasukkan jumlah Inputan
a = input('Masukkan jumlah inputan : ')

# Membuat list kosong untuk di input dari looping 
listKosong = []

# Membuat listSorted untuk menampung list yang sudah di sortir
listSorted = []


# Membuat def function Manual Sort dengan jumlah inputan dari inputan variable a
def manualSort(a):
    # Menentukan batasan input harus numeric dan nilai maksimal 100
    if a.isnumeric() and  int(a) <=100 :
        # Looping dari jumlah inputan yang ada di variabel a dimulai dari 1 sampai a (a+1 menandakan sampai sebelumnya)
        for i in range(1,int(a)+1):
            # Input untuk bilangan yang diinginkan sebanyak a (input awal jumlah)
            b = input('Angka ke - {} : '.format(i))
            if b.isnumeric() and int(b) <=100:
                # Append dari input diatas ke dalam list kosong
                listKosong.append(b)
                # Sorting listKosong dari kecil ke besar
                listKosong.sort()
                # Membuat variabel listSorted menjadi listKosong
                listSorted = listKosong
            else:
                # Break statement jika looping b tidak memenuhi numeric dan dibawah 100
                break
        # if statement untuk print hasil sorting jika numeric dan dibawah 100
        if b.isnumeric() and int(b) <=100:
            print('Hasil sort : ')
            # Print dengan cara kebawah
            print(*listSorted, sep = '\n')
        else:
            # Jika variabel b ada yang tidak numeric dan dibawah 100
            print('Invalid Input!')
    else :
        # Jika tidak memenuhi batasan input (numeric dan angka lebih besar dari 100)
        print('Invalid Input!')

# Menjalankan def function manualSort
manualSort(a)