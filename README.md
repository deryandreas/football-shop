TUGAS 2

1. Implementasi checklist step-by-step

Pertama, saya membuat sebuah fungsi pada views.py yang mengembalikan data berupa nama aplikasi serta nama dan kelas saya. Data tersebut kemudian saya hubungkan dengan sebuah template HTML agar bisa ditampilkan di browser. Setelah itu, saya menambahkan routing pada urls.py di dalam aplikasi main supaya URL tertentu dapat diarahkan ke fungsi yang sudah saya buat di views.py. Jika URL tersebut diakses, maka template yang berisi informasi tadi akan ditampilkan. Setelah aplikasi berjalan di lokal, saya melakukan deployment ke PWS dengan cara push project ke repository PWS menggunakan akun dan password PWS, sehingga aplikasi bisa diakses secara online. Terakhir, saya membuat file README.md yang berisi tautan aplikasi di PWS serta jawaban pertanyaan refleksi.

2. Bagan request–response Django

Alurnya seperti ini:

Client mengirim request ke server Django.

Request pertama kali masuk ke urls.py untuk dicocokkan dengan pola URL.

Jika cocok, request diteruskan ke fungsi yang sesuai di views.py.

Di dalam views.py, fungsi bisa mengambil/mengolah data dari models.py bila diperlukan.

Setelah itu, hasilnya dikirim ke template HTML untuk dirender menjadi tampilan.

Response HTML yang sudah jadi dikembalikan ke client (browser).

Kaitannya:

urls.py berfungsi sebagai “peta jalan” request.

views.py berperan sebagai “otak” yang mengatur logika dan menghubungkan data dengan template.

models.py menyimpan struktur data/database yang bisa diambil views.

Template HTML menampilkan data yang sudah diolah views ke user.

3. Peran settings.py

File settings.py adalah pusat konfigurasi Django. Isinya antara lain daftar aplikasi yang dipakai, konfigurasi database, static files, template path, security (secret key, debug mode, allowed hosts), hingga konfigurasi deployment. Intinya, semua pengaturan proyek Django diatur di sini.

4. Cara kerja migrasi database di Django

Migrasi database di Django bekerja dengan cara membandingkan model yang ada di models.py dengan struktur database yang sekarang. Jika ada perubahan (misalnya menambah field, membuat tabel baru, atau menghapus field), maka Django akan membuat file migrasi yang berisi instruksi perubahan. File migrasi tersebut bisa dijalankan agar database mengikuti perubahan yang ada di model, sehingga konsistensi antara kode dan database tetap terjaga.

5. Alasan Django dipilih sebagai framework pertama

Django dipilih karena sifatnya “batteries included”, artinya sudah menyediakan banyak fitur bawaan (autentikasi, ORM, template engine, dll.) sehingga memudahkan pemula untuk belajar. Django juga menekankan pola desain MTV (Model–Template–View) yang rapi, sehingga mahasiswa bisa memahami alur request–response web development dengan jelas. Selain itu, dokumentasi Django lengkap dan komunitasnya besar, membuatnya cocok untuk dijadikan pintu masuk mempelajari pengembangan perangkat lunak berbasis framework.


TUGAS 3

<img width="1919" height="1199" alt="Screenshot 2025-09-16 145339" src="https://github.com/user-attachments/assets/85af2cc3-e8e0-4244-b5b5-a04e2a3b3c31" />![WhatsApp Image 2025-09-16 at 14 53 45_66ce111e](https://github.com/user-attachments/assets/77981f01-0f3c-4cdb-be28-132476a07f3c)

<img width="1919" height="1199" alt="Screenshot 2025-09-16 145403" src="https://github.com/user-attachments/assets/787a19bc-bc3c-4cab-828f-8cadfa976ba1" />

<img width="1919" height="1199" alt="Screenshot 2025-09-16 150421" src="https://github.com/user-attachments/assets/a94a51c6-e07b-4fa9-9353-b98f6aa560ac" />

<img width="1919" height="1199" alt="Screenshot 2025-09-16 150445" src="https://github.com/user-attachments/assets/e0fbfd6f-01a1-4089-bc1b-7c3033f11f76" />


1.
Dalam pengembangan platform, data delivery diperlukan karena berfungsi sebagai penghubung antara backend dan frontend. Backend yang mengolah data perlu mengirim hasilnya dalam format yang bisa dimengerti oleh frontend. Dengan adanya data delivery, informasi bisa ditampilkan di web, aplikasi mobile, atau bahkan diakses sistem lain dengan mudah dan konsisten.

2.
JSON lebih baik dipakai di kebanyakan aplikasi modern karena formatnya lebih sederhana, lebih ringkas, dan langsung kompatibel dengan JavaScript. XML memang kuat untuk data yang punya struktur kompleks, tapi butuh parser tambahan dan lebih verbose. Popularitas JSON datang dari efisiensinya dalam pengiriman data, kecepatan parsing, dan kemudahan integrasi di hampir semua bahasa pemrograman.

3.
Method is_valid() pada form Django digunakan untuk mengecek apakah data yang dikirim pengguna sesuai aturan yang ditentukan di form atau model. Jika valid, data bisa diproses lebih lanjut. Jika tidak, Django memberi tahu bagian mana yang salah supaya pengguna bisa memperbaikinya. Tanpa validasi ini, data bisa berantakan atau bahkan berbahaya jika langsung disimpan.

4.
csrf_token dibutuhkan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Token ini memastikan bahwa request form benar-benar berasal dari pengguna yang sah, bukan dari situs luar yang mencoba memanfaatkan sesi pengguna. Jika tidak menggunakan csrf_token, penyerang bisa membuat halaman palsu yang secara diam-diam mengirimm request berbahaya ke server kita.

5.
Implementasi checklist saya lakukan step by step mulai dari membuat model Shop, lalu membuat form dengan ShopForm, menyiapkan views untuk create, list, dan detail data. Setelah itu, saya buat template HTML (main.html, create_shop.html, dan detail_shop.html) untuk menampilkan hasilnya. Selanjutnya saya menambahkan URL patterns di urls.py sesuai kebutuhan, lalu membuat endpoint untuk serialisasi data ke JSON dan XML, baik untuk semua data maupun berdasarkan ID. Semua langkah ini saya lakukan dengan memahami alurnya, bukan hanya sekadar copy-paste dari tutorial.


TUGAS 4

1. Apa itu Django AuthenticationForm? Kelebihan & Kekurangan

Deskripsi: AuthenticationForm adalah form bawaan Django (django.contrib.auth.forms.AuthenticationForm) untuk proses login. Menyediakan field username dan password, validasi kredensial menggunakan authentication backend, dan mendukung menerima request untuk validasi yang bergantung pada request.

Kelebihan: langsung pakai (plug-and-play), terintegrasi dengan sistem auth Django, menangani validasi & error message standar, sudah compatible dengan middleware/session Django.

Kekurangan: default memakai username (kalau mau pakai email perlu subclass/override), kurang fleksibel untuk fitur kompleks (2FA, captcha) tanpa extend, perlu adaptasi untuk custom user model tanpa username.

2. Perbedaan autentikasi vs otorisasi & bagaimana Django mengimplementasikannya

Autentikasi: proses verifikasi identitas — jawaban: “siapa pengguna ini?” Django: authenticate() + login() + User model + authentication backends + AuthenticationForm. Hasil autentikasi dicatat di session.

Otorisasi: proses pengecekan hak/izin — jawaban: “apa yang boleh dilakukan pengguna ini?” Django: permission system (user.has_perm()), Group, field is_staff/is_superuser, decorator @permission_required/@login_required. Untuk object-level permission perlu tambahan atau implementasi khusus (mis. django-guardian).

Interaksi: autentikasi memberi identity; otorisasi memakai identity tersebut untuk memutuskan akses ke resource/aksi.

3. Kelebihan & kekurangan session vs cookies (penyimpanan state)

Cookies (client-side):

Kelebihan: persist di client, tidak butuh penyimpanan server, cocok untuk preferensi ringan.

Kekurangan: terbatas ukuran (~4KB), rentan tampering/XSS jika tidak aman, tidak cocok untuk data sensitif.

Sessions (server-side, cookie hanya menyimpan session id):

Kelebihan: data disimpan di server (lebih aman untuk data sensitif), cookie kecil (session id) saja, kontrol penuh di server.

Kekurangan: butuh storage/management di server (skalabilitas), perlu cleanup/garbage collection, manajemen replikasi jika banyak instance.

Rekomendasi: minimalkan data pada cookie; gunakan session untuk state sensitif; atur atribut keamanan cookie.

4. Apakah cookies aman secara default? Risiko & bagaimana Django menanganinya

Risiko: XSS (steal cookie), CSRF (aksi tak sah), session fixation, sniffing di koneksi non-HTTPS.

Django mitigasi: CSRF middleware & token, SESSION_COOKIE_HTTPONLY = True (default) untuk mencegah akses JS, opsi SESSION_COOKIE_SECURE & CSRF_COOKIE_SECURE (aktifkan di HTTPS), SESSION_COOKIE_SAMESITE untuk mitigasi CSRF, session server-side sehingga cookie hanya session key. Namun developer tetap harus konfigurasi (aktifkan HTTPS, set Secure/HttpOnly/SameSite, jangan simpan data sensitif di cookie) — cookies tidak aman “tanpa konfigurasi” di environment produksi.


5. Saya mengimplementasikan checklist dengan dimulai dari memastikan konfigurasi environment database sudah benar lalu menjalankan migrasi agar tabel terbentuk, kemudian menambahkan relasi user pada model produk dan melakukan migrasi ulang; setelah itu saya membuat fitur registrasi dengan validasi data dan login otomatis setelah berhasil daftar, dilanjutkan dengan fitur login yang menggunakan sistem autentikasi bawaan Django serta menyimpan cookie last_login, dan fitur logout yang menghapus sesi pengguna; pada halaman utama saya menampilkan informasi pengguna yang sedang login beserta nilai cookie last_login serta membatasi produk yang tampil hanya milik user terkait; pengujian dilakukan dengan membuat dua akun berbeda dan masing-masing diberi tiga produk untuk memastikan data yang tampil sesuai user yang login; terakhir saya memastikan keamanan melalui proteksi CSRF bawaan Django serta prinsip penyimpanan cookie aman, kemudian seluruh proses ini saya dokumentasikan dalam README agar mudah dipahami tanpa sekadar mengikuti tutorial.

TUGAS 5

1. Urutan Prioritas Pengambilan CSS Selector
Urutan prioritas dalam pengambilan atau penerapan CSS Selector disebut Spesifisitas (Specificity), yaitu algoritma yang digunakan browser untuk menentukan aturan gaya mana yang harus diterapkan pada suatu elemen HTML. Spesifisitas bekerja berdasarkan bobot: Inline Styles memiliki bobot tertinggi dan mengalahkan semuanya; diikuti oleh ID Selector (#nama-id); kemudian Class Selector (.nama-kelas), Attribute, dan Pseudo-class Selector; dan yang terendah adalah Type Selector (nama tag seperti p atau div) dan Pseudo-element Selector. Browser selalu menerapkan gaya dari aturan yang memiliki bobot spesifisitas paling tinggi, atau, jika bobotnya sama, gaya dari aturan yang muncul terakhir dalam stylesheet.

2. Pentingnya Responsive Design
Responsive Design adalah konsep fundamental dalam pengembangan web modern yang memungkinkan layout dan tampilan situs beradaptasi secara mulus terhadap berbagai ukuran layar, mulai dari ponsel hingga monitor desktop. Konsep ini sangat penting karena mayoritas pengguna saat ini mengakses internet melalui perangkat seluler, dan situs yang tidak responsif akan memaksa pengguna untuk melakukan zoom atau scroll horizontal, menghasilkan pengalaman pengguna (UX) yang buruk dan mengurangi konversi. Contohnya, Shopee menerapkan desain responsif yang mengubah menu penuh menjadi ikon hamburger di ponsel, sementara situs kuno dengan lebar fixed (misalnya 960px) seringkali tidak responsif, membuat kontennya sulit dibaca di perangkat seluler.

3. Perbedaan antara Margin, Border, dan Padding
Ketiga properti ini mendefinisikan Box Model CSS yang mengatur ruang di sekitar elemen HTML. Padding adalah ruang internal yang berada di antara konten elemen dan border elemen tersebut; menambah padding akan memperbesar ukuran visual elemen. Border adalah garis bingkai yang mengelilingi padding dan konten; digunakan untuk membatasi elemen secara visual. Sementara itu, Margin adalah ruang eksternal di luar border, digunakan untuk menciptakan jarak antara elemen tersebut dengan elemen di sekitarnya; margin tidak memengaruhi ukuran elemen itu sendiri. Ketiganya diimplementasikan melalui CSS atau utility classes pada framework seperti Tailwind (misalnya: p-4 untuk padding, border-2 untuk border, dan m-4 untuk margin).

4. Konsep Flex Box dan Grid Layout
Flex Box (Flexible Box Layout) dan Grid Layout adalah modul CSS yang dirancang untuk mengatasi masalah layout kompleks. Flex Box dioptimalkan untuk layout satu dimensi (baik sebagai baris atau kolom), sangat ideal untuk mengatur, meratakan, dan mendistribusikan item di sepanjang sumbu tunggal, menjadikannya sempurna untuk membuat navigation bar atau footer. Sebaliknya, Grid Layout dirancang untuk layout dua dimensi (mengatur baris dan kolom secara simultan), memungkinkan penempatan dan perataan elemen yang lebih kompleks di dalam layout utama, membuatnya cocok untuk struktur halaman utama, dashboard, atau tata letak galeri produk yang membutuhkan kontrol terhadap kedua dimensi.

5. Penjelasan Langkah-demi-Langkah Implementasi Checklist
Implementasi fitur dan desain dilakukan secara bertahap, dimulai dengan fungsi CRUD (Create, Read, Update, Delete) yang dihubungkan melalui paths di urls.py ke fungsi di views.py, dengan tombol Edit/Delete hanya muncul pada kartu produk milik pengguna yang sedang login ({% if user.is_authenticated and shop.user == user %}). Selanjutnya, Kustomisasi Desain dilakukan menggunakan Tailwind CSS, menerapkan utility classes untuk merapikan halaman login dan register, membuat halaman daftar produk responsif dengan grid grid-cols-x dan logic {% if not shop_list %} untuk kondisi data kosong, serta memodifikasi card produk (card_shop.html) dengan perubahan minor pada shadow, border radius, dan penempatan badge agar tidak sama persis dengan desain tutorial. Terakhir, Navigation Bar Responsif dibuat dengan kelas Tailwind (md:hidden) dan fungsionalitas toggle menu diimplementasikan menggunakan JavaScript yang diletakkan di file eksternal (script.js), yang kemudian ditautkan di base.html, memastikan tombol hamburger hanya aktif di perangkat mobile dan mengubah ikonnya saat diklik.