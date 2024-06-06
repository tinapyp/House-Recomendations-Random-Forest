## Dokumentasi: Building a Content-Based Filtering Model

### Tujuan:
Tujuan dari proyek ini adalah untuk mengembangkan model filtering berbasis konten untuk memprediksi beberapa atribut rumah berdasarkan preferensi dan karakteristik konsumen.

### Langkah yang Diambil:

1. **Pemuatan Data:**
   - Data dimuat dari file CSV menggunakan library Pandas.

2. **Pra-Pemrosesan Data:**
   - Pembaruan Nama Kolom: Beberapa nama kolom diperbarui untuk kejelasan.
   - Menghapus Kolom yang Tidak Diperlukan: Kolom yang dianggap tidak diperlukan untuk model dihapus.
   - Seleksi Fitur: Fitur-fitur relevan termasuk usia, status pernikahan, jumlah anak, pendapatan per bulan, fasilitas yang diinginkan, dan preferensi lingkungan dipilih.

3. **Pengkodean Variabel Kategorikal:**
   - Pengkodean Label: Variabel kategorikal seperti status pernikahan dan pendapatan per bulan dikodekan menggunakan LabelEncoder.
   - Pengkodean One-Hot: Fasilitas yang diinginkan dan preferensi lingkungan dikodekan one-hot untuk mengubahnya menjadi fitur numerik yang sesuai untuk pemodelan.

4. **Penskalaan Fitur:**
   - Penskalaan Standar: Usia discaling menggunakan StandardScaler untuk memastikan semua fitur berada pada skala yang sama.

5. **Pemisahan Data Latih dan Uji:**
   - Dataset dibagi menjadi set data latih dan uji dengan rasio 80:20, masing-masing.

6. **Seleksi dan Pelatihan Model:**
   - Klasifikasi Random Forest: Random Forest dipilih sebagai model karena kemampuannya untuk menangani data kategorikal dan hubungan non-linear dengan efektif.
   - Model dilatih pada data latih.

7. **Evaluasi Model:**
   - Perhitungan Akurasi: Akurasi model dievaluasi secara terpisah untuk setiap output (Nama Perumahan, Jenis Rumah, Tipe Rumah).
   - Matriks Confusion: Matriks confusion dihasilkan untuk menilai kinerja model pada setiap output.

8. **Serialisasi Model:**
   - Model yang dilatih diserialkan menggunakan pickle untuk penggunaan di masa mendatang.

### Kesimpulan:
Secara keseluruhan, model filtering berbasis konten berhasil dibangun untuk memprediksi beberapa atribut rumah berdasarkan preferensi dan karakteristik konsumen. Model mencapai akurasi yang memuaskan, dan kinerjanya dievaluasi menggunakan matriks confusion