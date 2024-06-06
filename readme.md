**House Recommendations Random Forest**

**Deskripsi:**
Aplikasi FastAPI yang berfungsi sebagai layanan prediksi machine learning. Layanan ini mengekspos sebuah endpoint RESTful /predict yang menerima permintaan POST berisi data yang akan diprediksi. Setelah menerima permintaan, layanan menggunakan model machine learning yang telah dilatih sebelumnya untuk membuat prediksi pada data yang diberikan dan mengembalikan hasil prediksi ke klien.

**Features:**
- Mengekspos endpoint RESTful /predict untuk melakukan prediksi.
- Mendukung permintaan POST dengan payload JSON yang berisi data input.
- Menangani pra-pemrosesan data dan prediksi menggunakan model machine learning yang telah dilatih sebelumnya.
- Mengembalikan hasil prediksi dalam format JSON.

**Penggunaan:**
1. Pastikan file model machine learning yang telah dilatih (`model.pkl`) diletakkan di direktori `models`.
2. Mulai server FastAPI dengan menjalankan script `app.py`:
   ```
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```
3. Kirimkan permintaan POST ke endpoint `/predict` dengan data input dalam format JSON. Contoh:
   ```
   POST http://127.0.0.1:8000/predict
   {
         "Usia": 35,
         "Status Pernikahan": "Sudah Menikah",
         "Jumlah Anak": 2,
         "Pendapatan/Bulan": "Rp. 5.000.000 - Rp. 10.000.000",
         "Fasilitas Yang Diinginkan": "Garden Lounge, Masjid",
         "Preferensi Lingkungan": "Dekat Dengan Tempat Ibadah, Dekat Dengan Sarana Perbelanjaan"
   }

   {
  "namaPerumahan": "Qianna Residence 2",
  "jenisRumah": "Komersil",
  "tipeRumah": "30/60"
   }

```
   ```
   Gantilah data input dengan nilai-nilai yang diinginkan.
   
4. Server akan merespons dengan hasil prediksi dalam format JSON.

````

```
    {
         "Usia": 35,
         "Status Pernikahan": "Sudah Menikah",
         "Jumlah Anak": 2,
         "Pendapatan/Bulan": "Rp. 5.000.000 - Rp. 10.000.000",
         "Fasilitas Yang Diinginkan": "CCTV 24 Jam & Security, One Gate System, Jalan Utama Yang Lebar, Jalan Menggunakan Paving Block, TK",
         "Preferensi Lingkungan": "View Pegunungan, Suasana Sejuk Dan Asri, Dekat Dengan Pusat Kota, Dekat Dengan Exit Tol, Dekat Dengan ATM Center, Dekat Dengan Sarana Pendidikan, Dekat Dengan Sarana Kesehatan, Dekat Dengan Sarana Perbelanjaan, Dekat Dengan Tempat Wisata, Dilalui Dengan SPBU"
   }

   {
  "namaPerumahan": "Setiabudi Estate",
  "jenisRumah": "Komersil",
  "tipeRumah": "36/72"
   }
```

   {
         "Usia": 28,
         "Status Pernikahan": "Lajang",
         "Jumlah Anak": 0,
         "Pendapatan/Bulan": "Rp. 2.000.000 - Rp. 5.000.000",
         "Fasilitas Yang Diinginkan": "CCTV 24 Jam & Security, TK",
         "Preferensi Lingkungan": "Dekat Dengan ATM Center, Dekat Dengan Tempat Kuliner"
   }

   {
  "namaPerumahan": "Goalpara Hiills",
  "jenisRumah": "Subsidi",
  "tipeRumah": "30/60"
   }

```
   
   {
         "Usia": 28,
         "Status Pernikahan": "Lajang",
         "Jumlah Anak": 0,
         "Pendapatan/Bulan": "Rp. 2.000.000 - Rp. 5.000.000",
         "Fasilitas Yang Diinginkan": "CCTV 24 Jam & Security, Jalan Utama Yang Lebar",
         "Preferensi Lingkungan": "Dekat Dengan Exit Tol, Dekat Dengan Sarana Perbelanjaan"
   }

   {
  "namaPerumahan": "Bukit Pinus Banjaran",
  "jenisRumah": "Subsidi",
  "tipeRumah": "30/60"
   }

```

   {
         "Usia": 27,
         "Status Pernikahan": "Sudah Menikah",
         "Jumlah Anak": 1,
         "Pendapatan/Bulan": "Rp. 2.000.000 - Rp. 5.000.000",
         "Fasilitas Yang Diinginkan": "CCTV 24 Jam & Security, Jalan Utama Yang Lebar, Jalan Menggunakan Paving Block",
         "Preferensi Lingkungan": "View Pegunungan, Suasana Sejuk Dan Asri, Dekat Dengan Pusat Kota, Dekat Dengan Sarana Pendidikan, Dekat Dengan Sarana Kesehatan, Dekat Dengan Sarana Perbelanjaan, Dekat Dengan Tempat Kuliner, Dilalui Dengan SPBU"
   }

   {
  "namaPerumahan": "Bukit Cibadak Asri",
  "jenisRumah": "Subsidi",
  "tipeRumah": "30/60"
   }



```````````````
{
         "Usia": 35,
         "Status Pernikahan": "Sudah Menikah",
         "Jumlah Anak": 1,
         "Pendapatan/Bulan": "Rp. 5.000.000 - Rp. 10.000.000",
         "Fasilitas Yang Diinginkan": "CCTV 24 Jam & Security, One Gate System, Jalan Utama Yang Lebar, Jalan Menggunakan Paving Block, Taman Bermain Anak, TK, Masjid, Garden Lounge, Smart Door Lock, Smart Home System",
         "Preferensi Lingkungan": "View Pegunungan, Suasana Sejuk Dan Asri, Dekat Dengan Pusat Kota, Dekat Dengan Exit Tol, Dekat Dengan ATM Center, Dekat Dengan Sarana Pendidikan, Dekat Dengan Sarana Kesehatan, Dekat Dengan Sarana Perbelanjaan, Dekat Dengan Tempat Ibadah, Dekat Dengan Tempat Kuliner, Dekat Dengan Tempat Wisata, Dilalui Dengan Kendaraan Umum, Dilalui Dengan SPBU"
   }

   {
   "namaPerumahan": "Setiabudi Estate",
   "jenisRumah": "Komersil",
   "tipeRumah": "36/72"
   }

**Data inputan**
1. Usia: Bebas

2. Status Pernikahan: 
Sudah Menikah
Lajang

3. Jumlah Anak: Bebas

4. Pendapatan/Bulan:
Rp. 2.000.000 - Rp. 5.000.000
Rp. 5.000.000 - Rp. 10.000.000
> Rp. 10.000.000

5. Fasilitas:
CCTV 24 Jam & Security
One Gate System
Jalan Utama Yang Lebar
Jalan Menggunakan Paving Block
Taman Bermain Anak
TK
Masjid
Garden Lounge
Smart Door Lock
Smart Home System

6. Lingkungan:
View Pegunungan
Suasana Sejuk Dan Asri
Dekat Dengan Pusat Kota
Dekat Dengan Exit Tol
Dekat Dengan ATM Center
Dekat Dengan Sarana Pendidikan
Dekat Dengan Sarana Kesehatan
Dekat Dengan Sarana Perbelanjaan
Dekat Dengan Tempat Ibadah
Dekat Dengan Tempat Kuliner
Dekat Dengan Tempat Wisata
Dilalui Dengan Kendaraan Umum
Dilalui Dengan SPBU

````

**Docker:**
1. Buat docker menggunakan dockerfile
   ```
   docker build -t api-ml:v1.0 -f Dockerfile .
   ```
2. Jalankan docker file
   ```
   docker run -p 80:8000 api-ml:v1.0

