from kasus_variabel import validasi_nama_variabel
from kasus_email import validasi_email
from kasus_hp import validasi_nomor_hp

def cetak_jejak(teks: str, jejak: list, diterima: bool):
    print(f"\nInput        : {teks!r}")
    print("Jejak State  : " + " -> ".join(jejak))
    print(f"State Akhir  : {jejak[-1]}")
    print(f"Hasil        : {'VALID (ACCEPT)' if diterima else 'TIDAK VALID (REJECT)'}")
    print("-" * 60)

def main():
    while True:
        print("\n" + "=" * 50)
        print("    PROGRAM VALIDASI INPUT MENGGUNAKAN DFA")
        print("=" * 50)
        print("1. Validasi Nama Variabel")
        print("2. Validasi Format Email Sederhana")
        print("3. Validasi Nomor HP Indonesia")
        print("4. Keluar")
        print("-" * 50)
        
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            teks = input("Masukkan nama variabel: ").strip()
            diterima, jejak = validasi_nama_variabel(teks)
            cetak_jejak(teks, jejak, diterima)
        elif pilihan == "2":
            teks = input("Masukkan email: ").strip()
            diterima, jejak = validasi_email(teks)
            cetak_jejak(teks, jejak, diterima)
        elif pilihan == "3":
            teks = input("Masukkan nomor HP: ").strip()
            diterima, jejak = validasi_nomor_hp(teks)
            cetak_jejak(teks, jejak, diterima)
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()