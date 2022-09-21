# PBP Tugas 3

Nama : Davyn Reinhard Santoso

NPM : 2106751083

Kelas : PBP - C

# 🔗 Links
[Tugas 3 Deployment - HTML](https://pbptugastiga.herokuapp.com/mywatchlist/html/)

[Tugas 3 Deployment - XML](https://pbptugastiga.herokuapp.com/mywatchlist/xml/)

[Tugas 3 Deployment - JSON](https://pbptugastiga.herokuapp.com/mywatchlist/json/)

[Tugas 3 Repository](https://github.com/dreins/PBPTugas2.git)


# Jawaban

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
Dalam mata kuliah PBP, kita dikenalkan dengan istilah - istilah seperti JSON, XML, dan HTML. Pada dasarnya, XML dan JSON berbeda dengan HTML, dimana XML dan JSON merupakan salah dua dari format pertukaran data. HTML sendiri merupakan jenis format yang ditujukan untuk tampilan dari data. HTML tidak memiliki rincian detail dari data, sedangkan XML dan JSON memilikinya. Kita telah mengetahui bahwa HTML berbeda dengan XML dan JSON, sehingga kita dapat mendalami lagi apa perbedaan XML dan JSON. 

Perbedaan utamanya sendiri terletak pada jenis bahasa yang digunakan, dimana XML tidak digunakan dengan bahasa pemrograman, tetapi dengan bahasa markup seperti HTML. JSON sendiri merupakan singkatan JavaScript Object Notation, dimana JSON dibangun dengan bahasa pemrograman JavaScript. JSON menggunakan konsep mapping menggunakan key dan value, layaknya dictionary pada python, tidak seperti XML yang menggunakan struktur pohon(tree structure) dengan tag layaknya struktur HTML. JSON sendiri lebih low-level, namun memiliki fleksibilitas yang lebih tinggi daripada XML seperti dapat mengakses array, kecepatan prosesnya mengalahkan XML, dan tanpa memiliki ketentuan namespace.

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Pada dasarnya, kita harus mengetahui dulu tentang apa itu data delivery. Data delivery adalah sebuah istilah untuk proses perpindahan data dari sumber data atau database pusat menuju kepada sisi pengguna dengan tujuan tertentu dan berlaku dua arah. Sebelumnya, saya sendiri telah menjelaskan dalam Tugas 1 bahwa platform merupakan hasil gabungan dari perangkat keras dan lunak dimana hasil ini akan menjadi wadah bagi suatu program aplikasi. Sebuah platform sendiri pastinya dibangun dengan memiliki tujuan tertentu. Tanpa data, sebuah platform hanya dapat berfungsi sebagai landing page yang statis saja. Bahkan, pembuatan landing page sendiri memerlukan data untuk ditampilkan. Oleh karena itu, data delivery akan mendukung platform untuk menjadi lebih interaktif dan dinamis dalam memenuhi tujuan awal dibentuknya platform tersebut. 

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi `mywatchlist` dengan menjalankan script ini pada direktori Tugas 2 
```bash
    python manage.py startapp mywatchlist
```

2. Menambahkan path aplikasi `mywatchlist` ke list **INSTALLED_APPS** pada `settings.py` milik folder `project_django`
```bash
    python manage.py startapp mywatchlist
```

3. Membuat sebuah class model MyWatchList seperti berikut

```python
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()
```

- watched : Menggunakan BooleanField() karena hanya terdapat dua status, yaitu sudah atau belum tertonton
- title : Menggunakan CharField() dengan maksimum 255 character karena judul film tidak sepanjang deskripsi, field ini akan membantu menghemat memori
- rating : Menggunakan TextField()

4. Melakukan aktivasi model pada program dengan cara menjalankan kode berikut pada cmd 
```bash
    python manage.py makemigrations
    python manage.py migrate
```

5. Menambahkan 10 data dengan cara membuat folder bernama `fixtures` dalam `mywatchlist` dan membuat file `mywatchlist_data.json`. Di file `mywatchlist_data.json`, pengisian 10 data tadi akan dilakukan dengan format key mengikuti model yang telah dibuat sebelumnya.

6. Setelah data dibuat, saya menjalankan kode berikut agar data yang telah dibuat dapat terdeteksi oleh `manage.py`.
```bash
    python manage.py loaddata mywatchlist_data.json
```

7. Melakukan import terhadap beberapa package dari python dan membuat fungsi - fungsi untuk mengembalikan format HTML, XML, dan JSON pada `views.py`

    - Import `HttpResponse` dan `serializers`
    ```python
        from django.http import HttpResponse
        from django.core import serializers
    ```

    - Membuat fungsi HTML, XML, dan JSOn yang menerima parameter *request*
    ```python
        def show_mywatchlist_html(request):
            .
            .
            .
            .
        return render(request, 'mywatchlist.html', context)
    ```

    ```python
        def show_watchlist_xml(request):
            .
            .
            .
            .
        return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")
    ```

    ```python
        def show_watchlist_json(request):
            .
            .
            .
            .
        return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")
    ```

    - Membuat folder `templates` dan membuat files format HTML bernama `mywatchlist.html` untuk menjadi template dari fungsi HTML

8. Membuat file `urls.py` dan membuat path-nya dengan tujuan routing kepada fungsi yang telah dibuat pada `views.py`
```python
    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_mywatchlist, name='mywatchlist'),
        path('html/', show_mywatchlist_html, name='mywatchlist'),
        path('xml/', show_watchlist_xml, name='mywatchlist'),
        path('json/', show_watchlist_json, name='mywatchlist'),
    ]
```






