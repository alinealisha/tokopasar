# TokoPasar 
link PWS: http://alisha-aline-tokopasar.pbp.cs.ui.ac.id/

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repository baru di GitHub dengan nama yang sesuai dengan toko yang akan dibuat.
2. Membuat folder atau direktori lokal dengan nama yang sama seperti repository di GitHub.
3. Melakukan konfigurasi Git di direktori lokal dengan mengatur username dan email menggunakan terminal.
4. Mengubungkan direktori lokal dengan repository GitHub.
5. menginisiasi proyek baru Django di dalam direktori lokal.
6. Membuat file main.html di dalam folder templates (dibuat didalam folder main pada direktori lokal) yang berisi nama dan kelas.
7. Mengubah kode dalam models.py dengan menambahkan model Product yang memiliki atribut sesuai kebutuhan toko seperti nama, harga, rating.
8. Melakukan migrasi model menggunakan perintah python manage.py migrate.
9. Membuat fungsi show_main di views.py yang menampilkan nama, kelas, nama toko, dan tambahan seperti rating toko.
10. Memetakan fungsi show_main di urls.py untuk routing URL aplikasi.
11. Melakukan deployment aplikasi ke PWS setelah semua konfigurasi selesai.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![image](https://github.com/user-attachments/assets/3b28d6b7-e55f-4bae-8ed4-d624b2e75703)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dalam pengembangan perangkat lunak, Git berfungsi sebagai version control yang melacak perubahan kode, memfasilitasi kolaborasi antar developer di cabang terpisah, dan mendukung pengembangan fitur serta perbaikan bug.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai framework awal karena *open source*, memungkinkan pengembangan yang sangat cepat, lengkap dengan berbagai fitur bawaan, aman dengan perlindungan *built-in*, dan serbaguna untuk berbagai jenis aplikasi web.

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (*Object Relational Mapping*) karena menghubungkan antara objek pada Python dengan tabel database sehingga akan mempermudah pengelolaan data tanpa perlu menulis query SQL secara langsung.
