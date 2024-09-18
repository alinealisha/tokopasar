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


# Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dalam pengimplementasian suatu platform berfungsi untuk memastikan informasi dapat terkirim dengan cepat, aman, dan efisien. Ini memungkinkan konektivitas antar sistem seperti server, basis data, dan aplikasi, sehingga komponen-komponen tersebut dapat beroperasi secara sinkron. Selain itu, data delivery juga memastikan transaksi dapat berlangsung dengan akurat, terutama pada platform seperti e-commerce dan perbankan, serta menjaga keamanan data agar terlindung dari risiko kebocoran ataupun kerusakan. 

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON
- Memiliki sintaks yang lebih sederhana dan lebih mudah dibaca oleh manusia ataupun mesin dibandingkan dengan XML.
- Didukung langsung oleh JavaScript yang mana merupakan bahasa pemrograman yang paling banyak digunakan untuk mengembangkan suatu website. Hal ini mempermudah developer bekerja dengan JSON tanpa memerlukan parsing tambahan.
- Dapat secara langsung diubah menjadi objek dalam banyak bahasa pemrograman seperti JavaScript, Python, dan PHP.
  
XML
- Mendukung struktur data yang lebih kompleks, seperti memiliki banyak atribut dan elemen.
- Sering digunakan dalam sistem lintas platform dan lintas aplikasi karena didukung oleh banyak protokol standar.
- Lebih disarankan untuk digunakan untuk dokumen yang memerlukan format yang kaya dan terstruktur, seperti konfigurasi aplikasi
- Tidak bergantung pada bahasa pemrograman tertentu sehingga dapat digunakan secara luas dalam berbagai lingkungan pengembangan.

Kesimpulannya adalah, JSON lebih baik dibandingkan dengan XML apabila digunakan untuk aplikasi website modern yang membutuhkan pertukaran data yang cepat dan ringan. XML lebih baik digunakan untuk keperluan dalam aplikasi yang memerlukan struktur data yang lebih kompleks dan validasi data yang lebih ketat. JSON lebih populer dibandingkan dengan XML karena lebih ringan, mudah dipahami, lebih efisien digunakan dalam aplikasi website modern saat ini.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang sudah dimasukkan ke dalam form memenuhi semua kriteria validasi yang telah ditentukan sebelumnya. Method ini dibutuhkan untuk menjamin konsistensi data, menghindari masalah keamanan, dan mempermudah pengelolaan pesan error. is_valid() memastikan bahwa data yang diinput melalui form aman dan sesuai aturan sebelum diproses lebih lanjut di dalam aplikasi Django.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Tanpa csrf_token, aplikasi rentan terhadap serangan ini, yang dapat mengakibatkan pencurian atau manipulasi data. Penyerang memanfaatkan kekurangan ini untuk mengirimkan permintaan yang tidak sah atas nama pengguna, menyebabkan kerusakan ataupun penyalahgunaan data. csrf_token memastikan bahwa permintaan yang mengubah data berasal dari sumber yang sah sehingga meningkatkan keamanan aplikasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat direktori baru dengan nama Templates pada direktori utama proyek tokopasar dan buat file baru didalamnya dengan nama base.html sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web.
2. Menambahkan pengaturan di settings.py dengan menambahkan direktori Templates ke dalam pengaturan DIRS.
3. Memperbarui isi dari main.html dengan menambahkan tag {% extends %} dan {% block content %} untuk mendefinisikan bagian konten halaman.
4. Menambahkan import uuid ke dalam models.py, lalu melakukan migrasi model untuk menerapkan perubahan.
5. Membuat file baru dengan nama forms.py yang berada di dalam direktori main untuk mendefinisikan formulir proyek dan menyimpan data formulir sebagai objek.
6. Menambahkan beberapa import ke dalam file views.py dan membuat suatu fungsi yang menerima parameter request.
7. Memperbarui fungsi show_main dengan menambahkan Product.objects.all() untuk mengambil semua objek dari database.
8. Mengimpor fungsi yang telah dibuat sebelumnya dan menambahkannya kedalam path URL ke variabel urlpatterns di dalam file urls.py.
9. Membuat file baru dengan nama create_product_entry.html di dalam direktori Templates yang ada di dalam direktori main.
10. Menambahkan fungsi show_xml ke dalam views.py dan menambahkan path URL untuk XML ke dalam urls.py
11. Menambahkan fungsi show_json ke dalam views.py dan menambahkan path URL untuk JSON ke dalam urls.py.
12. Menambahkan fungsi show_xml_by_id dan show_json_by_id untuk mengembalikan data dalam XML dan JSON berdasarkan ID. Lalu, tambahkan path URL ke dalam file urls.py
13. Menggunakan Postman untuk menguji keempat endpoint GET yang telah dibuat sebelumnya.
14. Melakukan push ke Github dan juga PWS.

Berikut adalah hasil akses URL pada Postman
![Screenshot (186)](https://github.com/user-attachments/assets/dbd1bd8e-d0a2-49f3-a1be-d8d5f5f8c023)
![Screenshot (187)](https://github.com/user-attachments/assets/8ec48580-0d95-4d54-aa39-5d261459e679)
![Screenshot (188)](https://github.com/user-attachments/assets/01d0427f-9435-49ce-8aa9-f2758dc9e616)
![Screenshot (189)](https://github.com/user-attachments/assets/68c05772-a21f-4a6f-816f-a5453a63a7c7)




