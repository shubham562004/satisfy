def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initial gap size

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap size

# Example usage:
my_list = [12, 34, 54, 2, 3]
shell_sort(my_list)
print("Sorted list:", my_list)
