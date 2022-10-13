# PBP Tugas 6

Nama : Davyn Reinhard Santoso

NPM : 2106751083

Kelas : PBP - C

# 🔗 Links
[Tugas 2 Deployment](https://pbptugasdua.herokuapp.com/todolist/)

[Tugas 2 Repository](https://github.com/dreins/PBPTugas2.git)


# Jawaban

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming merupakan tipe programming yang memberi kesempatan kepada pengguna untuk berinteraksi secara langsung dengan website di saat sisi pengguna dan server dari website sedang melakukan pemrosesan data, sedangkan synchronous programming merupakan kebalikan dari asynchronous programming dimana pengguna harus menunggu pemrosesan data sehingga proses eksekusi tidak dapat dijalankan langsung secara bersamaan.

### 2.  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan sebuah konsep pemrograman dimana jalannya program tersebut akan ditentukan oleh faktor - faktor eksternal dari luar seperti aksi pengguna. Salah satu contoh penerapan Event-Driven Programming dalam tugas 6 ini adalah penampilan modal untuk menambahkan task. Modal akan muncul apabila pengguna melakukan trigger dengan meng-click tombol.

### 3.  Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX dapat dilihat dengan jelas pada konsep get dan post milik AJAX. Pengguna dapat berinteraksi dengan website untuk mengambil dan mengirimkan data ketika program juga melakukan pengambilan data berupa JSON yang tersedia.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat function baru pada `views.py` dengan mengganti return berupa `JsonResponse` 
```bash
    return JsonResponse()
```

2. Menambahkan `<script>` pada file html `todolist.html` dan instalasi ajax
    `https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js`

3. Mengisi tag `<script>` lanjutan dengan function JavaScript yang mengembalikan get dan post
```JavaScript
     function createTask() {
        $.post({
            url:
            ...
```

4. Melakukan integrasi pada `urls.py` terkait

5. Memasukkan id pada function JavaScript kepada tag terkait

