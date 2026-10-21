# Implementasi Deterministic Finite Automata (DFA) untuk Validasi Input

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Course](https://img.shields.io/badge/Course-Teori%20Komputasi-orange)
![Institution](https://img.shields.io/badge/Universitas-Sebelas%20Maret-green)

Proyek ini merupakan implementasi **Deterministic Finite Automata (DFA)** menggunakan bahasa pemrosesan Python untuk memvalidasi tiga bentuk sintaks masukan secara prediktif dan tepat. Proyek ini disusun untuk memenuhi tugas mata kuliah **Teori Komputasi**.

---

## 👥 Anggota Kelompok 9

| Nama Lengkap | NIM | Peran / Kontribusi |
| :--- | :--- | :--- |
| **Sulthan Hafizh Putra Agung** | K3525013 | Anggota Kelompok |
| **Zahra Faizza Kuncoroningrum** | K3525017 | Anggota Kelompok |
| **Wijang Pratama Putra** | K3525043 | Anggota Kelompok |

* **Dosen Pengampu:** Dr. Dwi Maryono, S.Si., M.Kom.  
* **Program Studi:** Pendidikan Teknik Informatika dan Komputer (PTIK)  
* **Fakultas:** Keguruan dan Ilmu Pendidikan, Universitas Sebelas Maret  

---

## 📚 Deskripsi Studi Kasus DFA

Aplikasi ini mencakup 3 fungsi validasi berbasis mesin keadaan terhingga deterministik (DFA):

### 1. Validasi Nama Variabel (`kasus_variabel.py`)
* **Aturan Sintaks:**
  * Karakter pertama wajib berupa huruf (`a-z`, `A-Z`) atau *underscore* (`_`).
  * Karakter berikutnya boleh berupa huruf, angka (`0-9`), atau *underscore* (`_`).
  * Tidak boleh memuat simbol lain maupun spasi.
* **Formal 5-Tuple:** $M_1 = (Q, \Sigma, \delta, q_0, F)$
  * $Q = \{q_0, q_1, q_{trap}\}$
  * $\Sigma = \{a..z, A..Z, 0..9, \text{'\_'}, \text{simbol lain}\}$
  * State Awal: $q_0$
  * $F = \{q_1\}$

---

### 2. Validasi Format Email Sederhana (`kasus_email.py`)
* **Aturan Sintaks:**
  * **Username:** Karakter alfanumerik, minimal 1 karakter.
  * **Simbol `@`:** Tepat satu simbol `@`.
  * **Domain:** Karakter alfanumerik, minimal 1 karakter.
  * **Titik (`.`):** Tepat satu simbol titik setelah domain.
  * **Ekstensi:** Huruf alfabet, minimal 2 karakter (misal: `com`, `id`, `org`).
* **Formal 5-Tuple:** $M_2 = (Q, \Sigma, \delta, q_0, F)$
  * $Q = \{q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_{trap}\}$
  * $\Sigma = \{a..z, A..Z, 0..9, \text{'@'}, \text{'.'}, \text{simbol lain}\}$
  * State Awal: $q_0$
  * $F = \{q_6\}$

---

### 3. Validasi Nomor HP Indonesia (`kasus_hp.py`)
* **Aturan Sintaks:**
  * Karakter ke-1 wajib digit `'0'`.
  * Karakter ke-2 wajib digit `'8'`.
  * Karakter ke-3 hingga seterusnya wajib berupa angka (`0-9`).
  * Panjang total nomor harus berada dalam rentang **10 hingga 13 digit**.
* **Formal 5-Tuple:** $M_3 = (Q, \Sigma, \delta, q_0, F)$
  * $Q = \{q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_{10}, q_{11}, q_{12}, q_{13}, q_{trap}\}$
  * $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \text{non-digit}\}$
  * State Awal: $q_0$
  * $F = \{q_{10}, q_{11}, q_{12}, q_{13}\}$

---

## 📁 Struktur Direktori

```text
.
├── kasus_variabel.py   # Modul DFA Validasi Nama Variabel
├── kasus_email.py      # Modul DFA Validasi Email Sederhana
├── kasus_hp.py         # Modul DFA Validasi Nomor HP Indonesia
├── main.py             # Program Utama & Antarmuka Menu Interaktif
└── README.md           # Dokumentasi Proyek
```

---

## 🚀 Cara Menjalankan Program

### Prasyarat
* Python 3.8 atau versi yang lebih baru.

### Langkah-Langkah

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/dfa-input-validation.git
   cd dfa-input-validation
   ```

2. **Jalankan program utama:**
   ```bash
   python main.py
   ```

3. **Pilih menu interaktif** yang tersedia di terminal untuk menguji validasi input secara langsung.

---

## 💻 Contoh Tampilan Output

```text
==================================================
    PROGRAM VALIDASI INPUT MENGGUNAKAN DFA
==================================================
1. Validasi Nama Variabel
2. Validasi Format Email Sederhana
3. Validasi Nomor HP Indonesia
4. Keluar
--------------------------------------------------
Pilih menu (1-4): 2
Masukkan email: budi123@gmail.com

Input        : 'budi123@gmail.com'
Jejak State  : q0 -> q1 -> q1 -> q1 -> q1 -> q1 -> q1 -> q1 -> q2 -> q3 -> q3 -> q3 -> q3 -> q3 -> q4 -> q5 -> q6 -> q6
State Akhir  : q6
Hasil        : VALID (ACCEPT)
------------------------------------------------------------
```
