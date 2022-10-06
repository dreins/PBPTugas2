# PBP Tugas 5

Nama : Davyn Reinhard Santoso

NPM : 2106751083

Kelas : PBP - C

# 🔗 Links
[Tugas 2 Deployment](https://pbptugasdua.herokuapp.com/todolist/)

[Tugas 2 Repository](https://github.com/dreins/PBPTugas2.git)


# Jawaban

### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
## 1. Inline CSS
Merupakan jenis CSS yang kodenya dituliskan langsung dalam atribut HTML

Kelebihan :
- Proses loading website lebih cepat dikarenakan permintaan HTTP yang kecil
- Memudahkan programmer melakukan debugging

Kekurangan :
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML

## 2. Internal CSS
Merupakan jenis CSS yang ditulis langsung dalam tag `<style>` dengan kode deklarator `<html>` di bagian atas file html.

Kelebihan :
- Baik untuk pengembangan yang membutuhkan kerumitan tinggi karena perubahan CSS hanya diterapkan pada satu halaman saja
- Tidak perlu melakukan upload file ulang karena HTML dan CSS berada dalam satu file

Kekurangan :
- Tidak efisien dalam pembuatan beberapa file saat menggunakan CSS yang sama
- Menyebabkan loading yang berat karena program harus menjalankan banyak CSS


## 3. External CSS
Merupakan jenis CSS yang kodenya ditulis terpisah dengan file HTML-nya, yaitu pada sebuah file khusus dengan ekstensi `.css`

Kelebihan :
- Penggunaan CSS dapat diterapkan pada beberapa halaman website tanpa harus diulang
- Proses loading website menjadi lebih cepat

Kekurangan:
- Dapat menyebabkan design yang berantakan ketika CSS gagal dipanggil oleh file terkait

### 2.  Jelaskan tag HTML5 yang kamu ketahui.
- `<a></a>` : Membuat hyperlink menuju halaman lain
- `<button></button>` : Membuat button yang dapat di-klik dan memiliki aksi
- `<form></form>` : Mendeklarasikan formulir untuk menerima input pengguna
- `<nav></nav>` : Membuat navigation bar pada aplikasi website
- `<div></div>` : Sebagai pembagi dan penggabung antara komponen yang satu dengan lainnya
- `<label></label>` : Membuat tulisan untuk ditampilkan sebagai label
- `<input></input>` : Membuat tempat untuk menerima input atau aksi dari pengguna
- `<link></link>` : Mendefinisikan hubungan dokumen dan sumber dari luar
- `<style></style>` : Mendefinisikan style design dan informasi untuk dokumen terkait
- `<svg></svg>` : Kontainer untuk gambar format SVG

### 3.  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Tag Selector, yaitu selector yang menggunakan tag HTML sebagai selectornya
2. Class Selector, yaitu selector yang memilih elemen berdasarkan nama class
3. ID Selector, yaitu selector yang menggunakan nomor unik ID untuk memilih elemen
4. Universal selector, yaitu selector yang berguna untuk menjangkau semua file HTML yang dituju
5. Attribute Selector, yaitu selector yang memilih elemen berdasarkan atribut

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Mengaktifkan virtual env menggunakan perintah 
```bash
    env\Scripts\activate.bat
```

2. Menjalankan perintah instalasi Tailwind CSS mengikuti website berikut
    `https://django-tailwind.readthedocs.io/en/latest/installation.html`

3. Mengisi tag milik Tailwind pada file templates utama, yaitu `base.html`
```HTML
    {% load tailwind_tags %}
    ...
    <head>
        ...
        {% tailwind_css %}
    ...
    </head>
```

4. Melakukan penghiasan pada file html


