def binary_search(data, target):
    indeks_kiri = 0
    indeks_kanan = len(data) - 1

    while indeks_kiri <= indeks_kanan:
        indeks_tengah = (indeks_kiri + indeks_kanan) // 2

        if data[indeks_tengah] == target:
            return indeks_tengah
        elif data[indeks_tengah] < target:
            indeks_kiri = indeks_tengah + 1
        else:
            indeks_kanan = indeks_tengah - 1

    return -1

def pemeriksa(hasil, target):
    if hasil != -1:
        print(f'{target} ditemukkan di index {hasil}')
    else:
        print('Data tidak ditemukan di array')


def main():
    # Data tidak urut
    unsorted_data = [12, 5, 19, 3, 8, 14]

    # Data urut menaik
    ascending_order = [1, 2, 3, 4, 5, 6, 7]

    # Target pencarian
    target = 7

    # Pemanggilan fungsi
    hasil = binary_search(ascending_order, target)
    pemeriksa(hasil, target)

if __name__ == "__main__":
    main()