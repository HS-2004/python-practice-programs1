def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

while True:
    print("\nMenu:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Exit")
    
    choice = input("Enter your choice (1,2,3,4,or 5): ")

    if choice == '1':
        array = list(map(int, input("Enter space-separated numbers: ").split()))
        sorted_array = selection_sort(array.copy())
        print("Sorted array using Selection Sort:", sorted_array)
    elif choice == '2':
        array = list(map(int, input("Enter space-separated numbers: ").split()))
        sorted_array = insertion_sort(array.copy())
        print("Sorted array using Insertion Sort:", sorted_array)
    elif choice == '3':
        array = list(map(int, input("Enter space-separated numbers: ").split()))
        sorted_array = merge_sort(array.copy())
        print("Sorted array using Merge Sort:", sorted_array)
    elif choice == '4':
        array = list(map(int, input("Enter space-separated numbers: ").split()))
        sorted_array = quick_sort(array.copy())
        print("Sorted array using Quick Sort:", sorted_array)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1,2,3,4,or 5.")
