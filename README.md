# 🇮🇩 Search Engine App :speech_balloon:
![halaman pertama Search.txt](/readme-material/homepage.png)

## Daftar isi
- [Tentang Mesin Pencarian (Search engine) :grey_question:](#tentang-mesin-pencarian-search-engine-grey_question)
- [Sebelum memulai](#sebelum-memulai)
- [Cara Memakai](#cara-memakai)
- [Author](#author)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Tentang Mesin Pencarian (Search engine) :grey_question:
Mesin pencarian adalah website yang mengumpulkan dan mengorganisir konten dari seluruh bagian dari internet.
Mesin pencarian merupakan cara untuk temu balik informasi.

*Temu-balik informasi* (information retrieval): menemukan kembali (retrieval) informasi yang relevan terhadap kebutuhan pengguna dari suatu kumpulan informasi secara otomatis.

Mesin pencarian ini memodelkan `query` dan `term` sebagai model ruang vektor. Dengan menggunakan [cosine similiarity](https://en.wikipedia.org/wiki/Cosine_similarity) untuk perhitungannya. Kami belum akan menjelaskan secara detail disini.

Pada dasarnya website yang kami buat ini menerima `query` dari pengguna dan me-*ranking* masukan file-file `.txt` berbahasa inggris.

## Sebelum memulai

![installation tutorial](/readme-material/installation.gif)

Pastikan sudah menginstall hal-hal berikut pada perangkat yang digunakan
- Python terinstall, jika belum dapat mendownload melalui link [berikut](https://www.python.org/downloads/)
- Python `pip` terinstall
- Flask terinstall, bisa dengan cara `pip install flask` pada terminal
- Install nltk module, bisa dengan cara `pip install nltk`
- Install nltk function fungsi berikut digunakan untuk *stemming* string
    - Buka IDE python ketikkan
        - import nltk
        - nltk.download('punkt')
        - nltk.download('stopwords')

## Cara Memakai

### Langkah-langkah Instalasi :
![Clone and running](/readme-material/clone.gif)

- Clone repository ini pada terminal : `git clone https://github.com/mhmmdjafarg/SearchEngineApp.git`
- Buka directory folder website `src`, kemudian jalankan pada terminal `python app.py`
- Secara default website akan dijalankan pada `http://127.0.0.1:5000/`


### Langkah pencarian :
![Clone and running](/readme-material/search.gif)

- Siapkan file berekstensi `.txt` yang akan dicari similiarity-nya, gunakan text berbahasa inggris :gb:
- Upload file yang telah disiapkan, (file tersebut sementara akan disimpan pada directory website pada folder `src/uploads`)
- Pada search bar, ketikkan query yang diinginkan, Go Search
- Untuk mencari dengan file lain, tekan tombol `reset` terlebih dahulu untuk menghapus file lama.
- Enjoy :thumbsup:

## Author

[Muhammad Jafar - 13519197](https://github.com/mhmmdjafarg)

[Faris Hasim - 13519050](https://github.com/farishasim)

[Randy Zakya - 13519061](https://github.com/rdyzakya)

📌 Bandung, Indonesia



