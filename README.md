Football Shop - Toko Olahraga BeliYuk

Aplikasi ini implementasi Tugas 2 PBP Semester Ganjil 2025/2026, Fakultas Ilmu Komputer UI. Tema: Football Shop, menjual item olahraga sepak bola seperti sepatu dan bola.

- Tautan Aplikasi
- Repo: https://github.com/ganeshatq/football-shop
- Web: https://ganesha-taqwa-footballshop.pbp.cs.ui.ac.id/

- Implementasi Checklist Step-by-Step
1. Buat proyek Django baru: `django-admin startproject football_shop .`.
2. Buat app `main`: `python manage.py startapp main`, tambah ke `INSTALLED_APPS` di `settings.py`.
3. Routing proyek: Di `football_shop/urls.py`, tambah `path('', include('main.urls'))`.
4. Model `Product` di `main/models.py`: Atribut `name` (CharField), `price` (IntegerField), `description` (TextField), `thumbnail` (URLField, blank/null=True), `category` (CharField), `is_featured` (BooleanField, default=False). Jalankan `makemigrations` & `migrate`.
5. Fungsi view di `main/views.py`: `show_main` fetch `Product.objects.all()`, buat context dengan app_name, npm, name, class, products; render ke `main.html`.
6. Routing app: Di `main/urls.py`, `path('', views.show_main, name='show_main')`.
7. Deploy ke PWS: Push ke GitHub, setup di PWS panel.
8. Tambah unit test di `tests.py` untuk URL, template, model; jalankan `python manage.py test`.

- Bagan Request Client ke Web Django

Request → urls.py (mencari alamat) → views.py (memproses logika) → models.py (mengambil data) → views.py (menggabungkan data dengan template) → template.html (membentuk tampilan) → Response.

link bagan: https://drive.google.com/drive/folders/1k0m97lW--0NXPEJE4oc-tY9Ps7mYFt50

- Peran settings.py
File settings.py adalah pusat konfigurasi utama dalam sebuah proyek Django yang berfungsi sebagai otak dari seluruh aplikasi.Di dalam file inilah semua pengaturan fundamental didefinisikan, mulai dari detail koneksi database yang digunakan, daftar aplikasi yang terpasang (INSTALLED_APPS), kunci keamanan (SECRET_KEY), hingga mode DEBUG untuk pengembangan. Selain itu, file ini juga mengatur bagaimana Django menangani file statis seperti CSS dan JavaScript, mengelola template, dan mengonfigurasi middleware yang memproses setiap request dan response, menjadikannya file pertama yang dirujuk untuk mengubah perilaku inti proyek.

- Cara Kerja Migrasi Database di Django
Sistem migrasi database di Django bekerja sebagai alat untuk mengelola perubahan skema database secara terstruktur dan sinkron dengan models.py. Proses ini dimulai dengan perintah makemigrations, yang akan mendeteksi perubahan pada model Anda dan secara otomatis membuat file migrasi berisi instruksi dalam bahasa Python. Setelah file instruksi ini dibuat, perintah migrate kemudian akan mengeksekusinya dengan cara menerjemahkan kode Python tersebut menjadi perintah SQL yang sesuai dan menerapkannya pada database, sehingga struktur tabel selalu konsisten dengan definisi model Anda.

- Mengapa Django untuk Permulaan Pembelajaran
Django sering dianggap sebagai framework yang ideal untuk pemula karena filosofinya yang "sudah termasuk baterai" (batteries-included) dan strukturnya yang terorganisir. Pendekatan ini menyediakan hampir semua komponen penting secara bawaan—seperti panel admin, ORM untuk interaksi database, dan sistem autentikasi—sehingga pemula bisa langsung fokus membangun fitur tanpa harus merakit banyak komponen terpisah. Ditambah dengan pola arsitektur Model-View-Template (MVT) yang jelas, dokumentasi yang sangat baik, serta fitur keamanan bawaan yang kuat, Django menawarkan jalur pembelajaran yang terstruktur dan mengajarkan praktik pengembangan perangkat lunak yang baik sejak awal.

- Feedback untuk Asisten Dosen Tutorial 1
...

Tugas 3

Tentu, ini adalah versi teks yang sudah rapi dan siap untuk Anda salin.

Pentingnya Data Delivery dalam Implementasi Platform

Dalam membangun sebuah platform digital, *data delivery* memegang peranan krusial sebagai jembatan komunikasi antar komponen. Proses ini memastikan bahwa semua bagian sistem—mulai dari antarmuka pengguna (*frontend*), logika server (*backend*), hingga layanan eksternal—dapat bertukar informasi secara efisien dan aman. Tanpa mekanisme pengiriman data yang terstruktur, integrasi sistem akan terhambat dan komunikasi antar bagian menjadi tidak lancar, sehingga platform tidak dapat berfungsi sebagaimana mestinya.

Perbandingan Antara JSON dan XML

Saat ini, JSON (JavaScript Object Notation) lebih sering menjadi pilihan utama dibandingkan XML (eXtensible Markup Language), terutama dalam pengembangan aplikasi web modern. Alasannya, format JSON lebih ringkas, mudah dibaca oleh manusia, dan lebih cepat diproses oleh mesin, khususnya oleh JavaScript yang merupakan bahasa utama di sisi *frontend*. Ukuran datanya yang lebih kecil juga membuat transfer data menjadi lebih efisien. Di sisi lain, XML memiliki struktur yang lebih kaku dan verbose (panjang), yang membuatnya kurang praktis untuk aplikasi yang mengutamakan kecepatan. Meskipun begitu, XML masih sangat relevan untuk sistem yang memerlukan struktur dokumen yang kompleks dan terperinci.

Fungsi Metode `is_valid()` pada Form Django

Metode `is_valid()` pada form Django adalah gerbang validasi utama sebelum data diproses lebih lanjut. Fungsinya adalah untuk memverifikasi apakah setiap data yang dikirimkan melalui form telah memenuhi semua aturan yang ditetapkan, seperti tipe data yang benar, panjang karakter yang sesuai, atau format yang valid. Jika semua data lolos validasi, metode ini akan mengembalikan nilai `True` dan menyimpan versi data yang sudah bersih dan aman dalam atribut `cleaned_data`. Proses ini sangat penting untuk mencegah entri data yang salah atau berbahaya masuk ke dalam *database*.

Pentingnya `csrf_token` untuk Keamanan Form Django

`csrf_token` adalah mekanisme pertahanan esensial dalam Django untuk mencegah serangan *Cross-Site Request Forgery* (CSRF). Token ini menghasilkan sebuah kode unik yang disematkan pada setiap form. Ketika form dikirim, Django akan memverifikasi apakah token yang diterima cocok dengan yang seharusnya. Tanpa token ini, aplikasi menjadi sangat rentan. Seorang penyerang dapat membuat halaman web palsu yang berisi form tersembunyi yang secara otomatis mengirim permintaan ke aplikasi Anda (misalnya, untuk mengubah data) menggunakan sesi *login* pengguna yang sedang aktif. Karena permintaan tersebut datang dari *browser* pengguna yang sah, server akan menganggapnya sebagai tindakan yang valid. Dengan `csrf_token`, permintaan palsu seperti ini akan langsung ditolak karena tidak memiliki token yang benar.

Langkah-Langkah Implementasi Proyek Django

Berikut adalah alur kerja yang saya terapkan dalam membangun fitur pada proyek Django:
1.  Inisiasi Kerangka Proyek: Saya mulai dengan membangun fondasi, yaitu membuat direktori `templates` di level proyek, mendaftarkannya di `settings.py`, dan membuat file `base.html` sebagai kerangka utama.
2.  Mendefinisikan Model Data Form: Selanjutnya, saya merancang struktur data yang akan diterima dari pengguna pada file `forms.py` dengan mendefinisikan *field* yang dibutuhkan seperti `"name"`, `"price"`, dan `"description"`.
3.  Membangun Logika Aplikasi (Views): Di `views.py`, saya menulis fungsi `create_product` untuk memproses data dari form dan `show_product` untuk mengambil serta menampilkan detail produk.
4.  Mengatur Rute URL: Agar fungsi-fungsi di *views* dapat diakses, saya mendaftarkannya di `urls.py` dengan membuat *path* URL yang sesuai untuk setiap fungsi.
5.  Merancang Antarmuka Pengguna (Templates): Saya mengembangkan tampilan HTML, memperbarui `main.html` untuk menampilkan daftar produk, serta membuat `create_product.html` untuk form input dan `product_detail.html` untuk halaman detail.
6.  Implementasi Serialisasi Data (JSON & XML): Untuk menyediakan data dalam format lain, saya membuat fungsi baru di `views.py` seperti `show_json` dan `show_xml` yang mengambil data, mengubahnya menjadi format yang diinginkan, dan mengirimkannya sebagai respons. Fungsi serupa juga dibuat untuk mengambil data berdasarkan ID tertentu, dengan penanganan *error* menggunakan `try-except`. Terakhir, semua fungsi ini didaftarkan pada `urls.py`.

Umpan Balik untuk Asisten Dosen

Tidak ada umpan balik yang ingin saya sampaikan untuk tutorial kedua ini. Semuanya sudah berjalan dengan baik. Hehe.

link ss postman: https://drive.google.com/drive/folders/1Q6ozRzldjHx81FjPCQVwqUi85XafZzWe?usp=sharing