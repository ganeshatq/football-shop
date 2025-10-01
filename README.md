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

Tugas 3

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


Tugas 4 


### Memahami Django AuthenticationForm

AuthenticationForm adalah sebuah form bawaan dari Django yang dirancang khusus untuk proses login pengguna. Formulir ini secara standar menyediakan dua kolom yaitu nama pengguna (username) dan kata sandi (password). Ketika pengguna mengirimkan data melalui formulir ini, Django akan menggunakan fungsi `authenticate()` untuk memverifikasi apakah kredensial tersebut valid.

Kelebihan

Proses login menjadi aman dan praktis, keamanannya sudah teruji, integrasi mudah dengan LoginView, dan terdapat dukungan berbagai backend autentikasi.

Kekurangan

Form ini hanya dirancang untuk login, sehingga tidak bisa dipakai untuk registrasi pengguna baru. Tampilan defaultnya sangat sederhana sehingga hampir selalu perlu diubah agar sesuai desain aplikasi, dan fitur ekstra seperti “remember me”, pembatasan percobaan login, atau autentikasi ganda harus ditambahkan secara manual atau dengan paket pihak ketiga.


### Perbedaan Autentikasi dan Otorisasi di Django

Dalam pengembangan aplikasi web, autentikasi dan otorisasi adalah dua konsep keamanan yang berbeda namun saling melengkapi.

Autentikasi adalah proses untuk memverifikasi siapa Anda. Ini adalah langkah pertama di mana sistem memastikan identitas pengguna, biasanya melalui username dan password.

Otorisasi adalah proses untuk menentukan apa yang boleh Anda lakukan. Setelah identitas pengguna terverifikasi, sistem akan memeriksa hak akses atau izin yang dimiliki pengguna tersebut.

Sebagai contoh, memasukkan username dan password di halaman login adalah autentikasi. Setelah berhasil login, sistem yang memeriksa apakah Anda memiliki izin untuk mengakses halaman admin adalah otorisasi.

Implementasi di Django

Django menangani autentikasi dengan sistem login bawaan yang memeriksa identitas pengguna melalui fungsi seperti `authenticate()` dan `login()`. Setelah berhasil, Django menyimpan status login di sesi dan menyediakan objek `request.user` agar aplikasi tahu siapa yang sedang masuk.

Django menangani otorisasi dengan sistem perizinan (permissions) dan group. Setiap user bisa diberi hak akses tertentu, misalnya menambah, mengubah, atau menghapus data. Pengecekan hak ini dilakukan dengan cara seperti `@login_required` atau `user.has_perm()`. Django memastikan hanya pengguna yang berwenang yang dapat mengakses atau mengubah bagian tertentu dari aplikasi.


### Perbandingan Session dan Cookies untuk Penyimpanan Status

Cookies dan session adalah dua mekanisme utama untuk menyimpan informasi (status) pengguna di aplikasi web.

Cookies

Kelebihannya, data disimpan langsung di browser pengguna (client-side), sehingga tidak membebani server dan sangat cocok untuk menyimpan data kecil dan tidak sensitif. Kekurangannya, ukurannya terbatas (sekitar 4KB), selalu dikirim pada setiap permintaan HTTP yang dapat menambah beban jaringan, dan rentan terhadap manipulasi jika tidak diamankan dengan benar (misalnya, tanpa atribut HttpOnly atau koneksi HTTPS).

Session

Kelebihannya, data disimpan di sisi server, membuatnya lebih aman dari manipulasi pengguna. Browser hanya menyimpan ID sesi sebagai penanda. Session dapat menampung data yang lebih besar dan lebih kompleks, seperti status login atau keranjang belanja. Kekurangannya, membutuhkan ruang penyimpanan dan sumber daya di server. Jika aplikasi berjalan di beberapa server (load balancing), diperlukan konfigurasi tambahan untuk memastikan data sesi dapat diakses oleh semua server.


### Keamanan Cookies dan Penanganan oleh Django

Secara default, cookies tidak sepenuhnya aman dan memiliki beberapa risiko keamanan yang perlu diwaspadai, di antaranya adalah Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Penyadapan (Sniffing), dan Session Fixation.

Bagaimana Django Melindungi Aplikasi?

Django menyediakan serangkaian perlindungan bawaan untuk mengatasi risiko-risiko ini. Secara default, cookie sesi Django diatur sebagai HttpOnly. Pengaturan SESSION_COOKIE_SECURE dapat diaktifkan untuk memastikan cookie hanya dikirim melalui koneksi HTTPS yang aman. Django juga memiliki middleware CSRF yang aktif secara default untuk melindungi aplikasi dari serangan Cross-Site Request Forgery. Pengaturan SESSION_COOKIE_SAMESITE membantu mencegah browser mengirim cookie bersamaan dengan permintaan lintas situs. Django secara otomatis merotasi ID sesi setelah pengguna berhasil login untuk mencegah session fixation.


### Langkah-Langkah Implementasi Fitur Pengguna

Berikut adalah penjelasan langkah demi langkah mengenai implementasi fitur-fitur yang disebutkan:

a. Implementasi Fungsi Registrasi, Login, dan Logout

Untuk mengelola siklus hidup pengguna, saya membangun tiga fungsi utama. Untuk Registrasi, saya membuat sebuah view bernama `register` yang memanfaatkan `UserCreationForm` bawaan Django. View ini menampilkan formulir registrasi dan, setelah data valid dikirimkan, membuat akun pengguna baru. Tampilan formulir ini saya letakkan di template `register.html` dan URL-nya diatur di `urls.py`. Untuk Login, saya membuat view `login_user` yang menggunakan `AuthenticationForm`. View ini memvalidasi kredensial pengguna dengan fungsi `authenticate()` dan `login()`. Sama seperti registrasi, formulirnya berada di `login.html` dan URL-nya telah didaftarkan. Untuk Logout, fungsi `logout_user` dibuat sangat sederhana dengan memanggil fungsi `logout()` dari Django untuk mengakhiri sesi pengguna. Sebuah tombol logout ditambahkan ke template yang relevan dan dihubungkan ke URL yang sesuai. Untuk melindungi halaman-halaman penting, saya menggunakan decorator `@login_required` pada view yang bersangkutan. Ini memastikan hanya pengguna yang sudah login yang dapat mengakses halaman tersebut.

b. Menampilkan Informasi Pengguna dan Menggunakan Cookies

Untuk meningkatkan pengalaman pengguna, saya menampilkan nama pengguna yang sedang login dan waktu login terakhirnya. Caranya adalah dengan memodifikasi view `login_user`. Setelah login berhasil, saya mengatur dua cookies: `current_user` yang berisi nama pengguna dan `last_login` yang berisi timestamp saat itu. Pada view halaman utama, saya membaca nilai dari kedua cookies tersebut dan mengirimkannya ke template. Di dalam template `main.html`, saya menampilkan pesan sambutan yang berisi data dari cookies tersebut. Saat pengguna melakukan logout, cookie `last_login` akan dihapus.

c. Menghubungkan Model Produk dengan Pengguna

Agar setiap produk dapat dimiliki oleh seorang pengguna (penjual), saya memodifikasi model `Product`. Saya menambahkan sebuah kolom `user` yang merupakan `ForeignKey` ke model `User` bawaan Django. Setelah mendefinisikan relasi ini, saya menjalankan `makemigrations` dan `migrate` untuk memperbarui skema database. Selanjutnya, saya menyesuaikan view untuk membuat produk (`create_product`). Kini, setiap produk yang dibuat akan secara otomatis diatribusikan ke pengguna yang sedang login (`request.user`). Tampilan utama juga saya perbarui dengan filter, sehingga pengguna bisa melihat semua produk atau hanya produk yang mereka unggah.

d. Membuat Data Uji Coba

Untuk menguji fungsionalitas aplikasi, saya membuat dua akun pengguna yang berbeda melalui halaman registrasi. Setelah login dengan akun pertama, saya menambahkan tiga data produk. Kemudian, saya logout dan login dengan akun kedua, lalu menambahkan tiga produk lainnya. Proses ini memastikan bahwa setiap produk terhubung dengan benar ke pengguna yang membuatnya dan fitur filter produk berfungsi sebagaimana mestinya.



Tugas 5

#### **1. Prioritas Selector CSS (Spesifisitas)**

Urutan kekuatan selector CSS dalam menentukan gaya (style) sebuah elemen, dari yang paling prioritas hingga yang paling rendah, adalah sebagai berikut:

1.  **Inline Styles**: Atribut `style` yang ditulis langsung pada elemen HTML (contoh: `style="color: pink;"`).
2.  **ID Selectors**: Selector yang menargetkan ID unik sebuah elemen (contoh: `#navbar`).
3.  **Classes, Attribute Selectors, dan Pseudo-classes**: Termasuk selector kelas (contoh: `.test`), selector berdasarkan atribut (contoh: `[type="text"]`), dan status elemen (contoh: `:hover`).
4.  **Elements dan Pseudo-elements**: Selector yang menargetkan nama tag HTML (contoh: `h1`) dan elemen semu (contoh: `::before`, `::after`).
5.  **Universal Selector dan `:where()`**: Selector yang menargetkan semua elemen (contoh: `*`) atau selector dengan spesifisitas nol (contoh: `:where()`).

#### **2. Desain Responsif (Responsive Design)**

Desain responsif adalah sebuah pendekatan dalam pengembangan web yang memastikan tampilan situs dapat beradaptasi secara optimal di berbagai ukuran layar, mulai dari desktop, tablet, hingga smartphone. Konsep ini sangat penting karena pengguna modern mengakses web dari beragam perangkat. Tanpa desain yang responsif, pengalaman pengguna (UX) dapat menjadi buruk dan tidak konsisten.

  * **Contoh Aplikasi Responsif**: Instagram, Tokopedia.

#### **3. Konsep Box Model CSS**

Setiap elemen HTML dapat dianggap sebagai sebuah "kotak" yang terdiri dari empat lapisan utama:

  * **Margin**: Area transparan di bagian terluar yang menciptakan ruang antara elemen ini dengan elemen lainnya.
  * **Border**: Garis yang mengelilingi padding dan konten. Posisinya berada di antara margin dan padding.
  * **Padding**: Area transparan di sekitar konten yang memberikan ruang di dalam border. Posisinya berada di antara konten dan border.
  * **Content**: Isi dari elemen itu sendiri, seperti teks, gambar, atau video.

**Contoh Implementasi:**

```css
div {
    margin: 20px;       /* Ruang 20px di luar border */
    border: 15px solid green; /* Garis hijau setebal 15px */
    padding: 50px;      /* Ruang 50px di dalam border */
}
```

#### **4. Perbandingan Layout: Flexbox vs. Grid**

  * **Flexbox**: Menyediakan sistem tata letak (layout) **satu dimensi** untuk mengatur item dalam sebuah baris (row) atau kolom (column). Sangat cocok digunakan untuk komponen seperti *navbar*, header, atau footer.
  * **Grid**: Menyediakan sistem tata letak **dua dimensi** (baris dan kolom sekaligus) untuk mengatur konten dalam format seperti tabel. Sangat ideal untuk layout halaman yang kompleks seperti *dashboard* atau galeri foto.

#### **5. Langkah-Langkah Implementasi pada Proyek**

Berikut adalah alur kerja yang telah dilakukan untuk mengimplementasikan fitur dan styling pada aplikasi:

1.  **Integrasi Tailwind CSS**: Menambahkan Tailwind ke dalam proyek dengan menyisipkan script CDN pada file `base.html`.
2.  **Pembuatan Fungsi Views**: Membuat fungsi `edit_products` dan `delete_products` di dalam file `views.py` untuk menangani logika bisnis.
3.  **Konfigurasi URL**: Mendaftarkan fungsi `edit_products` dan `delete_products` ke dalam `urls.py` dan menambahkan path URL yang sesuai ke dalam `urlpatterns`.
4.  **Menghubungkan ke Template**: Mengintegrasikan fungsionalitas edit dan hapus ke dalam template `main.html` agar dapat diakses oleh pengguna.
5.  **Penambahan Komponen**: Membuat template untuk komponen *navbar* dan memasukkannya ke dalam struktur aplikasi.
6.  **Konfigurasi Static Files**: Mengatur pengelolaan file statis (seperti CSS, JavaScript, dan gambar) pada aplikasi.
7.  **Styling**: Melakukan penataan visual pada seluruh aplikasi dengan menggunakan *utility classes* dari Tailwind dan beberapa kustomisasi melalui file CSS eksternal.
