# Praktikum4
## Tugas Pertemuan 9 - Bahasa Pemrograman

### 1. File program
Program ini adalah program sederhana untuk menambahkan data kedalam sebuah list dengan menggunakan module texttable pada python.

* **CODINGAN:**
```
  from texttable import Texttable

 table = Texttable ()
 jawab = "y"
 no = 0
 nama = []
 nim = []
 nilai_tugas = []
 nilai_uts = []
 nilai_uas = []
 while(jawab == "y"):
     nama.append(input("Masukan Nama :"))
     nim.append(input("Masukan Nim  :"))
     nilai_tugas.append(input("Nilai Tugas  :"))
     nilai_uts.append(input("Nilai UTS    :"))
     nilai_uas.append(input("Nilai UAS    :"))
     jawab = input("Tambah data (y/t)?")
     no += 1
 for i in range(no):
     tugas = int(nilai_tugas[i])
     uts = int(nilai_uts[i])
     uas = int(nilai_uas[i])
     akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100) 
     table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])                                                                                                                                                                                                                                                                                                                                                
 print (table.draw())
```

* **Hasil output program:**

![Gambar 1](Screenshoot/ss1.png)

* **Flowchart:**

![Gambar 2](Screenshoot/flowchart.png)

* **Penjelasan program:**

Install terlebih dahulu module texttable dan PIP (Package) 

Pada langkah pertama kita perlu meng-import module yang telah di install dengan kodingan seperti dibawah ini.
```
 from texttable import Texttable
```

Lalu membuat sebuah variable seperti berikut.
```
 table = Texttable ()
 jawab = "y"
 no = 0
 nama = []
 nim = []
 nilai_tugas = []
 nilai_uts = []
 nilai_uas = []
```

Langkah selanjutnya membuat sebuah pengulangan dengan menggunakan perintah *while*, Dengan variable jawab yang berinput "y" bertujuan untuk mengulang pertanyaan.
```
 while(jawab == "y"):
```

Method list.append(obj) digunakan untuk menambahkan object obj ke dalam sebuah list pada kolom tabel.
```
 nama.append(input("Masukan Nama :"))
      nim.append(input("Masukan Nim  :"))
      nilai_tugas.append(input("Nilai Tugas  :"))
      nilai_uts.append(input("Nilai UTS    :"))
      nilai_uas.append(input("Nilai UAS    :"))
```

kodingan tesebut menghasilkan output dengan pertanyaan yang bertujuan untuk menambahkan data, jika jawab "y" maka pertanyaan akan terulang kembali dan diinput kembali seperti sebelumnya, jika menjawab "t" maka program tersebut akan berhenti secara otomatis dan menghasilkan ouput dari hasil yang telah diinput. dengan cara tersebut kita bisa menginput lebih dari 1 inputan atau sesuai dengan yang kita inginkan.
```
 jawab = input("Tambah data (y/t)?")
     no += 1
 for i in range(no):
 ```

kodingan tersebut merupakan sebuah output yang menghasilkan kolom tabel yang didalamnya berisikan Variable yang telah diinput seperti Nama, Nim, Nilai tugas, Nilai Uts, Nilai Uas, dan Nilai Akhir. pada perintah table.add_row' berguna menambahkan baris pada tabel, serta untuk perhitungan nilai akhir menggunakan operator aritmatika perkalian dan penjumlahan.
```
 tugas = int(nilai_tugas[i])
     uts = int(nilai_uts[i])
     uas = int(nilai_uas[i])
     akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100) 
     table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])        
```     
