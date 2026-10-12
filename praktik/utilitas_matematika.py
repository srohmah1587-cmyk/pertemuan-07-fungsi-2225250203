
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== MENU PROGRAM ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


# Program utama
tampilkan_menu()
pilihan = input("Pilih menu (1-4): ")

if pilihan == "1":
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    print("Luas persegi panjang =", luas_persegi_panjang(p, l))

elif pilihan == "2":
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    print("Luas segitiga =", luas_segitiga(a, t))

elif pilihan == "3":
    n = int(input("Masukkan nilai n: "))
    if n >= 1:
        print("Jumlah 1 sampai", n, "=", jumlah_n(n))
    else:
        print("n harus lebih dari atau sama dengan 1.")

elif pilihan == "4":
    n = int(input("Masukkan bilangan bulat nonnegatif: "))
    if n >= 0:
        print("Faktorial", n, "=", faktorial(n))
    else:
        print("n tidak boleh negatif.")

else:
    print("Pilihan tidak valid.")
    