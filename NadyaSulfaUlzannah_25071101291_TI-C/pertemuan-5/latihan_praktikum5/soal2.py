def kurang_matriks(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 

A = [[5, 3, 1], 
    [2, 8, 4], 
    [6, 0, 7]] 

B = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 

C_kurang = kurang_matriks(A,B)
print("pengurangan")
for baris in C_kurang:
    print(baris)