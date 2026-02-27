def kali_skalar(matriks, k): 
    hasil = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        hasil.append(baris_baru) 
    return hasil 

A = [[5, 3, 1], 
    [2, 8, 4], 
    [6, 0, 7]] 

B = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 

C_skalar = kali_skalar(A,4)
print("skalar")
print(C_skalar)