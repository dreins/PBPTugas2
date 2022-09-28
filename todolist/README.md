# PBP Tugas 4

Nama : Davyn Reinhard Santoso

NPM : 2106751083

Kelas : PBP - C

# 🔗 Links
[Tugas 2 Deployment](https://pbptugasdua.herokuapp.com/todolist/)

[Tugas 2 Repository](https://github.com/dreins/PBPTugas2.git)


# Jawaban

### 1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Pada dasarnya, CSRF merupakan singkatan dari Cross-Site Request Forger yang merupakan istilah dari serangan sederhana yang dapat dilakukan oleh hacker pada suatu website. CSRF token akan berguna untuk mencegah serangan tersebut, dimana CSRF akan mencegah hacker untuk melakukan request terhadap HTTP untuk memasukkan script dan mengumpankannya kepada program. Token ini memiliki wujud suatu kode rahasia yang unik dan susah untuk diakses oleh orang. Tanpa potongan kode tersebut, hacker akan mudah mengakses HTTP dari website yang kita buat, dimana menyebabkan mereka untuk mudah dalam memasukkan script tertentu dan melakukan hal yang mereka inginkan tanpa penghalang

### 2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Menurut saya, elemen `<form>` dapat dibuat secara manual. Secara gambaran besar, suatu form merupakan diletakkan dengan cara menginstansiasikan object pada framework Django. Secara manual, kita dapat membuat form melalui HTML dengan cara menuliskannya satu - satu dan menjalankan mekanisme pengambilan value dari tiap - tiap form seperti mekanisme POST pada Django.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Berdasarkan kode yang telah saya buat, seluruh submisi data pada form akan dipicu oleh keinginan user. Dalam hal ini, kita dapat melihat pada penggunaan syntax `request.user` untuk melakukan segala sesuatu pada task. Nantinya, dengan method `POST`, keinginan user akan dikirimkan kepada pusat atau database dari server. Nantinya, submisi yang dilakukan oleh user melalui HTML akan diterima oleh `views` dan `views` akan melakukan pekerjaannya untuk melakukan perubahan dan memberikan respon pada user. 

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi `todolist` dengan menjalankan script ini pada direktori Tugas 2 
```bash
    python manage.py startapp todolist
```

2. Menambahkan path aplikasi `todolist` ke list **INSTALLED_APPS** pada `settings.py` milik folder `project_django`
```bash
    INSTALLED_APPS = [
        .....,
        'todolist',
        .....,
    ]
```

3. Membuat sebuah class model Task seperti berikut, sesuai kriteria yang diberikan pada tugas

```python
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

- user : Menggunakan ForeignKey() agar user dapat berdiri secara independen
- date : Menggunakan DateField() dengan tambahan script `auto_now=True` agar tanggal dapat ditampilkan secara jelas pada program
- title : Menggunakan CharField() untuk judul
- description : Menggunakan TextField() untuk deskripsi
- is_finished : Menggunakan BooleanField() dengan tambahan script `default=False` karena task tidak mungkin di-POST jika telah selesai

4. Melakukan aktivasi model pada program dengan cara menjalankan kode berikut pada cmd 
```bash
    python manage.py makemigrations
    python manage.py migrate
```

5. Menambahkan 10 data dengan cara membuat folder bernama `fixtures` dalam `mywatchlist` dan membuat file `mywatchlist_data.json`. Di file `mywatchlist_data.json`, pengisian 10 data tadi akan dilakukan dengan format key mengikuti model yang telah dibuat sebelumnya.

6. Membuat fungsi - fungsi yang diperlukan pada `views.py` seperti
    ```python
        @login_required(login_url='/todolist/login/')
        def show_task(request):
            .........

        def register(request):
            .........

        def login_user(request):
            .........

        def logout_user(request):
            .........
        
        @login_required(login_url='/todolist/login/')
        def create_task(request):
            .........

        @login_required(login_url='/todolist/login/')
        def update(request, key):
            .........

        @login_required(login_url='/todolist/login/')
        def delete(request, key):
            .........
    ```

    

    - Membuat folder `templates` dan membuat files format HTML untuk menjadi template dari fungsi HTML

8. Membuat file `urls.py` dan membuat path-nya dengan tujuan routing kepada fungsi yang telah dibuat pada `views.py`
```python
    app_name = 'todolist'

    urlpatterns = [
        path('', show_task, name='show_task'),
        path('login/', login_user, name='login_user'),
        path('register/', register, name='register'),
        path('create-task/', create_task, name='create_task'),
        path('logout/', logout_user, name='logout_user'),
        path('update-task/<int:key>/', update, name='update'),
        path('delete-task/<int:key>/', delete, name='delete'),
    ]
```

9. Menambahkan url `todolist` dalam `urls.py` milik proyek, yaitu `project_django`

```python
    urlpatterns = [
        .........,
        path('todolist/', include('todolist.urls')),
        .........,
    ]
```


