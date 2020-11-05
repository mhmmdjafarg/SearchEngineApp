# SearchEngineApp

## Web requirements
- Template html home
- Search query bar, ada tombol submit
- Bagian untuk upload multiple files,ada tombol submit juga
- Tampilkan tabel --> ke endpoint baru
- link ke page profile
- gimana caranya file yang diupload dibuatkan link ke full text document tersebut

## Frontend trasfer data to backend
- Search query --> ubah ke string
- each files, jadikan string

## Data yang perlu ada di variables
- Judul dokumen (beserta link ke full text jadikan array)
- Jumlah kata tiap dokumen
- Tingkat kemiripan (cosine similiarity)
- Kalimat pertama dokumen

## Array yang dibutuhkan
- array of full text dokumen
- array of string dari semua kata (sudah di stemming)
- array of jumlah kata
- Bikin table seperti spesifikasi

## Fungsi yang dibutuhkan
- Fungsi ngubah input files ke string
- Fungsi ubah query ke string
- Fungsi stemming kata
- Fungsi untuk lowercase string
- Fungsi hitung jumlah kata -> masukin ke array jumlah kata contoh array[0] = query, arrray[1] = D1
- Fungsi hitung per kata jadiin tabel (kata, jumlahnya)
- Fungsi hitung panjang vektor dari tabel hitung perkata
- Fungsi perkalian dot Query dengan dokument
- Fungsi cosine sim pake 2 fungsi diatas ini

## Langkah Pengerjaan untuk cosine similiarity

1. stemming / hapus kata berimbuhan ga jelas
2. Buat menjadi lower case semua aja 
3. Hapus karakter tidak perlu seperti titik, koma dsb
4. Bahasa inggris
5. Masukan list kata nya kedalam satu array global `list_word`
6. Yang pertama kali ada dalam array global adalah list_word dari query
7. Hitung |Q| panjang vektor nya
8. Hitung setiap frekuensinya mengikuti indeks array global, jika tidak ada menjadi 0
9. Hitung juga jumlah katanya, simpan
10. buat menjadi tabel vektor (query dan dokumen dokumen)
11. Hitung |D| panjang vektor nya untuk dokumen
12. kali dot dengan vektor query (hitung cosine similiarity)
13. Simpan hasilnya
14. next dokumen
