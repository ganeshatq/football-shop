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