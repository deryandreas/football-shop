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