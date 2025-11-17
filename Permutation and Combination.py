print("NAMA  : RIFKI ADE TIA")
print("NIM   : 312510334")
print("KELAS : TI.25.C5")
print()
print("===PERMUTASI===")
print()
print("1. Dapatkan Semua Permutasi Daftar")
from itertools import permutations

perm = permutations([4, 5, 6])

for i in perm:
    print(i)
print()
print("2. Permutasi Dengan Panjang Tertentu")
from itertools import permutations

perm = permutations([4, 5, 6], 2)

for i in perm:
    print(i)
print()
print("===KOMBINASI===")
print()
print("1. Dapatkan Semua Kombinasi Panjang 2")
from itertools import combinations

comb = combinations([4, 5, 6], 2)

for i in comb:
    print(i)
print()
print("2. Kombinasi Dari Daftar Yang Tidak Diurutkan")
from itertools import combinations

comb = combinations([6, 4, 5], 2)

for i in comb:
    print(i)
print()
print("3. Kombinasi Dengan Pengulangan")
from itertools import combinations_with_replacement

comb = combinations_with_replacement([4, 5, 6], 2)

for i in comb:
    print(i)