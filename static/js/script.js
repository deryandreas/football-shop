document.addEventListener('DOMContentLoaded', () => {
    // 1. Ambil elemen tombol dan menu menggunakan ID
    // Pastikan ID 'mobile-menu-button' dan 'mobile-menu' sudah ada di navbar.html
    const button = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    // Pastikan kedua elemen ditemukan di DOM sebelum menambahkan event listener
    if (button && menu) {
        
        // Logic Utama: Toggle menu saat tombol diklik
        button.addEventListener('click', () => {
            // Toggle kelas 'hidden' untuk menampilkan/menyembunyikan menu (Tailwind)
            menu.classList.toggle('hidden');
            
            // Logic Mengubah Ikon (fa-bars <-> fa-times)
            const icon = button.querySelector('i');
            if (icon) {
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

        // Logic Tambahan: Tutup Menu Otomatis Saat Link di menu mobile Diklik
        menu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                // Tutup menu hanya jika sedang terbuka
                if (!menu.classList.contains('hidden')) {
                    menu.classList.add('hidden');
                    
                    // Kembalikan ikon ke hamburger
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