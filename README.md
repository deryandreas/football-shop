1.
Dalam pengembangan platform, data delivery diperlukan karena berfungsi sebagai penghubung antara backend dan frontend. Backend yang mengolah data perlu mengirim hasilnya dalam format yang bisa dimengerti oleh frontend. Dengan adanya data delivery, informasi bisa ditampilkan di web, aplikasi mobile, atau bahkan diakses sistem lain dengan mudah dan konsisten.

2.
JSON lebih baik dipakai di kebanyakan aplikasi modern karena formatnya lebih sederhana, lebih ringkas, dan langsung kompatibel dengan JavaScript. XML memang kuat untuk data yang punya struktur kompleks, tapi butuh parser tambahan dan lebih verbose. Popularitas JSON datang dari efisiensinya dalam pengiriman data, kecepatan parsing, dan kemudahan integrasi di hampir semua bahasa pemrograman.

3.
Method is_valid() pada form Django digunakan untuk mengecek apakah data yang dikirim pengguna sesuai aturan yang ditentukan di form atau model. Jika valid, data bisa diproses lebih lanjut. Jika tidak, Django memberi tahu bagian mana yang salah supaya pengguna bisa memperbaikinya. Tanpa validasi ini, data bisa berantakan atau bahkan berbahaya jika langsung disimpan.

4.
csrf_token dibutuhkan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Token ini memastikan bahwa request form benar-benar berasal dari pengguna yang sah, bukan dari situs luar yang mencoba memanfaatkan sesi pengguna. Jika tidak menggunakan csrf_token, penyerang bisa membuat halaman palsu yang secara diam-diam mengirim request berbahaya ke server kita.

5.
Implementasi checklist saya lakukan step by step mulai dari membuat model Shop, lalu membuat form dengan ShopForm, menyiapkan views untuk create, list, dan detail data. Setelah itu, saya buat template HTML (main.html, create_shop.html, dan detail_shop.html) untuk menampilkan hasilnya. Selanjutnya saya menambahkan URL patterns di urls.py sesuai kebutuhan, lalu membuat endpoint untuk serialisasi data ke JSON dan XML, baik untuk semua data maupun berdasarkan ID. Semua langkah ini saya lakukan dengan memahami alurnya, bukan hanya sekadar copy-paste dari tutorial.
