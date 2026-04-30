# INSERTTION SORT
def insertionsort(mylist):
  n = len(mylist)
  for i in range(1,n):
    insert_index = i
    current_value = mylist.pop(i)
    for j in range(i-1, -1, -1):
      if mylist[j] > current_value:
        insert_index = j
    mylist.insert(insert_index, current_value)


# QUICK SORT
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)


# COUNTING SORT
def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

# MAIN
jumlah = int(input("Masukkan jumlah elemen : "))

mylist = []
for i in range(jumlah):
  elemen = int(input(f"Masukkan elemen {i+1}:"))
  while elemen < 0:
    print("elemen yang di masukkan:")
    elemen = int(input(f"Masukkan elemen {i+1}"))

  mylist.append(elemen)

print("Sebelum diurutkan:", mylist)

copy01 = mylist.copy()
insertionsort(copy01)
print("insertion sort:", copy01)

copy02 = mylist.copy()
quicksort(copy02)
print("quick sort:", copy02)

mysortedlist = countingSort(mylist)
print("counting Sort", mysortedlist)