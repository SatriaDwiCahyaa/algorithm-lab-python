def linear_search(data, target):
    for indeks in range(len(data)):
        if data[indeks] == target:
            return indeks
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

    target = 8

    hasil = linear_search(unsorted_data, target)
    pemeriksa(hasil, target)


if __name__ == '__main__':
    main()