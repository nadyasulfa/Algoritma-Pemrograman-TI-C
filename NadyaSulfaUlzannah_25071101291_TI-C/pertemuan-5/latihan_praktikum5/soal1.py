def tambah_matriks(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]): 
        print('Error: ukuran matriks tidak sama') 
        return None 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 

A = [[5, 3, 1], 
    [2, 8, 4], 
    [6, 0, 7]] 

B = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 

C_tambah = tambah_matriks(A,B)
print("penambahan")
for baris in C_tambah:
    print(baris)


