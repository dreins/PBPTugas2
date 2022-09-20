# PBP Tugas 2

Nama : Davyn Reinhard Santoso

NPM : 2106751083

Kelas : PBP - C

# 🔗 Links
[Tugas 2 Deployment](https://pbptugasdua.herokuapp.com/katalog/)

[Tugas 2 Repository](https://github.com/dreins/PBPTugas2.git)


# Jawaban

### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![](assets/BaganPBPTugas2.png)

### 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan untuk membangun ekslusivitas antar beberapa orang yang membangun sebuah aplikasi website. Hal ini dilakukan untuk memastikan bahwa aplikasi website yang kita buat dapat berjalan dengan baik pada sistem operasi yang sama, meskipun pada dependencies yang berbeda - beda. Ibaratkan seorang bernama A dan seorang bernama B memiliki versi Library Python yang berbeda, maka eksklusivitas ini akan menjamin bahwa proyek dapat berjalan dalam lingkup mereka masing - masing tanpa perlu menyamakan versi dari sistem. 

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas
1. Pertama - tama, saya membuat sebuah fungsi bernama katalog dengan menggunakan variabel request yang dipanggil jika client mengakses URL. Dalam fungsi, saya menaruh suatu data yang nantinya berasal dari file .json ditambah dengan nama dan NPM. Fungsi ini mengembalikan request dan template html yang akan diisi dengan data yang saya taruh. Tidak lupa juga data yang saya taruh telah saya ekstrak dengan model yang tersedia terlebih dahulu

2. Setelah mengisi views.py, saya mendaftarkan nama routing yang ingin saya gunakan, yaitu "katalog/". Terlebih dahulu, saya mendaftarkan nama aplikasi pada route ini dengan nama 'katalog', selanjutnya saya mendaftarkan nama route tadi pada urlpatterns dengan memanggil fungsi katalog dari views.py untuk ditampilkan. Di akhir, saya melakukan pendaftaran nama aplikasi kepada program utama, yaitu settings.py dan urls.py di project_django

3. Setelah views.py, models.py, dan urls.py telah selesai untuk dikonfigurasi, kini giliran saya menyocokkan data - data dalam fungsi tadi kepada template html yang tersedia. Untuk konfigurasi, saya menggunakan bracket {{}} untuk memanggil data dari fungsi. Pada data terperinci dari models, saya menggunakan forloop untuk iterasi tiap data yang akan ditampilkan 

4. Ketika semuanya telah selesai, saya melakukan deploy pada website yang saya buat dengan diawali add, commit, dan push pada repository yang telah saya buat. Tidak lupa saya tambahkan file dpl.yml untuk konfigurasi Heroku ditambah dengan aksi pip freeze pada versi - versi library di requirements.txt. Selanjutnya, saya juga menambahkan PROJECT_ROOT dan STATIC_ROOT di settings.py project_django.Saat semuanya telah terkonfigurasi, saya membuat aplikasi baru pada Heroku berjudul pbptugasdua. Lalu, pada cmd folder terkait, saya melakukan login terhadap heroku dilanjutkan dengan perintah clone untuk menyambungkan folder dengan App Heroku. Di akhir, saya melakukan perintah git add, commit, dan push seperti di awal, bedanya adalah perintah ini menuju ke App Heroku yang ada dengan sedikit perbedaan sintaks

