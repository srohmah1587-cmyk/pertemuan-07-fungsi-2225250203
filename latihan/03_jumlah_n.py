
def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

daftar_n = [1, 5, 10, 100]

for n in daftar_n:
    hasil_perulangan = jumlah_n(n)
    hasil_rumus = n * (n + 1) // 2

    print("n =", n)
    print("Hasil perulangan =", hasil_perulangan)
    print("Hasil rumus =", hasil_rumus)
    print("Sama =", hasil_perulangan == hasil_rumus)
    print()
    