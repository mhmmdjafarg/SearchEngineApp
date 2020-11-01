# SearchEngineApp

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