#List dengan 5 elemen
print("="*35)
nilai = [11, 12, 13, 14, 15]
print("Membuat sebuah list dengan 5 elemen: ")
print(nilai[0:6])
print("="*35)

#Akses pada list
print("Akses list")
print ("element ke 3 : ", nilai[2])
print ("element ke 2 sampai ke 4 : ", nilai[1:4])
print("="*35)

#mengubah element list
print("Mengubah elemen list")
odd = [11,12,13,14,15]
odd[3] = 10
print("Mengubah elemen ke 4 dengan nilai lainnya: ", odd)

#Mengubah elemen ke 4 sampai dengan elemen terakhir
odd[3:5] = [16,18]
print("Mengubah elemen ke 4 sampai dengan elemen terakhir: ",odd)
print("="*30)

#menambahkan element
print("Menambahkan element")
nilaia = [11,22,14]
nilaib = [24,12,52]
print("list a : ", nilaia)
print("list b : ", nilaib)
nilaib.append(99)
print ("menambahkan list B nilai string : ", nilaib)
nilaib.extend([60,70,80])
print ("menambahkan list B dengan 3 nilai", nilaib)
print ("mengabungkan list A dan B : " ,nilaia + nilaib)
print("="*35)
print("Thanks :)")
print("="*35)