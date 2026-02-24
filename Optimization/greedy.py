import os
os.system('cls')


def get_jumlah_uang():
    while True:
        try:
            jumlah_uang = int(input('Masukkan jumlah uang: '))
            
            if jumlah_uang <= 0:
                print('Jumlah uang harus lebih dari 0')
                continue

            return jumlah_uang

        except ValueError:
            print('Masukkan Angka!')

def greedy_coin_change(jumlah):
    koin = [1000, 500, 200, 100]
    total_koin = 0

    for nilai in koin:
        jumlah_koin = jumlah // nilai
        jumlah = jumlah % nilai
        total_koin += jumlah_koin

        print(f'{nilai} : {jumlah_koin} Koin')

    print("\nTotal koin yang digunakan:", total_koin)


def main():
    user_money = 24500
    greedy_coin_change(user_money)

    input()


if __name__ == "__main__":
    main()