# Selection Sort Implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input using simple for loop
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("\nUnsorted array:", arr)

# Sort the array
selection_sort(arr)

# Print the sorted array
print("\nSorted array:", arr)
