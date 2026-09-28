"""Modul ini adalah contoh perbaikan kode agar lolos Pylint."""

GLOBAL_VAR = 10

def hitung_sesuatu(kondisi_a, kondisi_b, kondisi_c, nilai_e, nilai_f):
    """Fungsi perhitungan yang sudah dirapikan sesuai PEP 8.

    Args:
        kondisi_a (bool): Kondisi pertama.
        kondisi_b (bool): Kondisi kedua.
        kondisi_c (Any): Kondisi ketiga (None).
        nilai_e (list): List angka.
        nilai_f (int): Angka tambahan.

    Returns:
        int atau None: Hasil perhitungan.
    """
    tambahan_satu = 1
    tambahan_nol = 0

    if kondisi_a and not kondisi_b and kondisi_c is None:
        try:
            print("Kondisi terpenuhi!")
            return nilai_e[0] + nilai_f + tambahan_satu + tambahan_nol
        except IndexError:
            return None
    return None

def main():
    """Fungsi utama untuk menjalankan skrip."""
    hasil = hitung_sesuatu(True, False, None, [2], 3)
    print(f"Hasil: {hasil}")

if __name__ == "__main__":
    main()
