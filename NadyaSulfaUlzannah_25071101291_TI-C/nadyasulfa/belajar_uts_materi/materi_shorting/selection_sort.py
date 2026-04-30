#SELECTION SORT - MAXIMUM
def maxx_selection_sort(data):
    n = len(data)

    for i in range(0, n-1):
        max_index = 0

        for j in range(1, n-1):
            if data[j] > data[max_index]:
                max_index = j

        data[max_index], data[n - 1 -i] = data[n -1 -i], data[max_index]
    
    return data

data = [17,23,49,62,20]

print("Data sebelum di sort - Max:", data)
maxx_selection_sort(data)
print("Data sesudah di sort - max:", data)

#SSELECTION SORT - MINIMUM
def min_selection_sort(data):
    n = len(data)

    for i in range(0, n-1):
        min_index = 0
        for j in range(1, n-1):
            if data[min_index] < data[j]:
                min_index = j

            data[min_index], data[n - 1 - i] = data[n - 1 - i], data[min_index]

    return data

data =[77,23,20,55,1]

print("Data sebelum di sort Min:", data)
min_selection_sort(data)
print("Data sesudah disort Min:", data)