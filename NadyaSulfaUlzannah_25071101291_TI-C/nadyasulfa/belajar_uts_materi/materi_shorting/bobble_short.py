#BOBBLE SORT - ASCENDING
def bobble_sort_acs(data):
    n = len(data)

    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]

    return data

data = [17, 10,20,49, 32]

print("Data sebelum di sort - Ascending: ", data)
bobble_sort_acs(data)
print("Data setelah di sort - Ascending: ", data)

#BOBBLE SORT - DESCENDING
def bobble_sort_desc(daftar):
    n = len(daftar)

    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if (daftar[j], daftar[j+1]):
                daftar[j], daftar[j+1] = daftar[j+1], daftar[j]
    return daftar

daftar = [65,22,20,82]

print("Data sebelum di sort - Descending:", daftar)
bobble_sort_desc(daftar)
print("Data sesudah disort - Descending:", daftar)