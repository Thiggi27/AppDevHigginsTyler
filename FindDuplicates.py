from collections import Counter

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Load data
data = []
with open("p2.txt", 'r') as fin:
    data = [int(line.strip()) for line in fin]

print("Unsorted Array")
print(len(data), "items")

# Sort data using QuickSort
quickSort(data, 0, len(data) - 1)

# Count duplicates
counter = Counter(data)
count_duplicates = sum(count - 1 for count in counter.values() if count > 1)

print("Found", count_duplicates, "duplicates")
