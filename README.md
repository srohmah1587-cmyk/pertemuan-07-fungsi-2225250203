# Pertemuan 07 Fungsi Python

**Nama:** Siti Rohmah
**NIM:** 2225250203
**Kelas:** 3A

## Tujuan

Mempelajari dan menerapkan fungsi Python, parameter, nilai kembali (*return value*), serta *scope* variabel untuk membuat program yang modular, terstruktur, dan mudah dipahami.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code pada folder utama proyek:

```bash
python3 praktik/utilitas_matematika.py
```

## Struktur Fungsi

Program utilitas matematika terdiri atas beberapa fungsi yang memiliki tugas berbeda.

| Nama Fungsi                  | Parameter   | Nilai Return              | Keterangan                                                         |
| ---------------------------- | ----------- | ------------------------- | ------------------------------------------------------------------ |
| `luas_persegi_panjang(p, l)` | `p` dan `l` | `p * l`                   | Menghitung luas persegi panjang berdasarkan panjang dan lebar.     |
| `luas_segitiga(a, t)`        | `a` dan `t` | `0.5 * a * t`             | Menghitung luas segitiga berdasarkan alas dan tinggi.              |
| `jumlah_n(n)`                | `n`         | `total`                   | Menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan. |
| `faktorial(n)`               | `n`         | `hasil`                   | Menghitung faktorial bilangan menggunakan perulangan.              |
| `tampilkan_menu()`           | Tidak ada   | Tidak ada nilai eksplisit | Menampilkan daftar pilihan operasi matematika.                     |

Fungsi-fungsi tersebut menerima parameter sesuai kebutuhan, melakukan proses perhitungan, dan mengembalikan hasil menggunakan `return`, kecuali fungsi `tampilkan_menu()` yang bertugas menampilkan menu.

## Hasil Pengujian

| No. | Input                   | Hasil yang Diharapkan     | Hasil Aktual              | Status   |
| --- | ----------------------- | ------------------------- | ------------------------- | -------- |
| 1   | Panjang = 8, lebar = 5 | 40                        | 40                        | Berhasil |
| 2   | Alas = 10, tinggi = 6    | 30                        | 30                        | Berhasil |
| 3   | n = 10                  | 55                        | 55                        | Berhasil |
| 4   | n = 5 pada faktorial    | 120                       | 120                       | Berhasil |
| 5   | n = 0 pada fakorial       | 1 | 1 | Berhasil |

Pengujian dilakukan untuk memastikan setiap fungsi menghasilkan keluaran yang sesuai dengan perhitungan matematika. Hasil aktual pada tabel merupakan hasil yang diharapkan berdasarkan kode program dan perlu disesuaikan apabila hasil pengujian langsung berbeda.

## Refleksi

Bagian program yang menjadi lebih sederhana setelah dipisahkan menjadi fungsi adalah proses perhitungan luas persegi panjang dan luas segitiga. Perhitungan tersebut tidak perlu ditulis ulang di dalam program utama karena sudah dibuat dalam fungsi tersendiri. Program utama cukup menerima input, memanggil fungsi dengan parameter yang sesuai, dan menampilkan hasilnya.

Penggunaan fungsi juga membantu mengurangi pengulangan kode, mempermudah pengujian, dan membuat program lebih mudah diperbaiki. Selain itu, melalui latihan ini saya memahami bahwa parameter digunakan untuk menerima data, `return` digunakan untuk mengembalikan hasil perhitungan, dan *scope* membedakan variabel lokal di dalam fungsi dari variabel yang berada di luar fungsi.
