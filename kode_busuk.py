"""Modul ini berisi contoh fungsi penjumlahan yang sudah diperbaiki kualitas kodenya."""

def jumlahkan_angka(angka_pertama, angka_kedua):
    """Fungsi untuk menjumlahkan dua angka.

    Args:
        angka_pertama (int): Angka pertama yang akan dijumlahkan.
        angka_kedua (int): Angka kedua yang akan dijumlahkan.

    Returns:
        int: Hasil penjumlahan kedua angka.
    """
    hasil = angka_pertama + angka_kedua
    print(f"Hasil: {hasil}")
    return hasil

def main():
    """Fungsi utama program."""
    jumlahkan_angka(1, 2)

if __name__ == "__main__":
    main()
