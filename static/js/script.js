// main/static/js/script.js
// source: gemini

document.addEventListener('DOMContentLoaded', () => {
    // Ambil elemen dengan ID yang ditambahkan di navbar.html
    const button = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    if (button && menu) {
        button.addEventListener('click', () => {
            // **PENAMBAHAN UTAMA:**
            // classList.toggle('hidden') akan menghapus 'hidden' (menampilkan menu) 
            // jika ada, dan menambahkannya kembali (menyembunyikan menu) jika tidak ada.
            menu.classList.toggle('hidden');
            
            // **PENAMBAHAN (OPSIONAL) Ikon Animasi:**
            const icon = button.querySelector('i');
            if (icon) {
                // Periksa apakah menu sedang tersembunyi (kelas 'hidden' ada)
                if (menu.classList.contains('hidden')) {
                    // Menu tertutup: Tampilkan ikon hamburger
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                } else {
                    // Menu terbuka: Tampilkan ikon X
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                }
            }
        });
    }

    // **PENAMBAHAN (OPSIONAL) Tutup Menu Otomatis Saat Link Diklik:**
    if (menu) {
        menu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                // Hanya jalankan di mobile (asumsi button ada)
                if (button) {
                    menu.classList.add('hidden');
                    // Kembalikan ikon
                    const icon = button.querySelector('i');
                    if (icon) {
                         icon.classList.remove('fa-times');
                         icon.classList.add('fa-bars');
                    }
                }
            });
        });
    }
});