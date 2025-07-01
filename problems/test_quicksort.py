import random

def quicksort(arr, low, high):

    if low < high: # base case when the subarray is 1 or 0 elements
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot is the last element
    i = low - 1  # Index of smaller element

    for j in range(low, high):  # Up to high - 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is less than or equal to pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1


if __name__ == "__main__":

    rand_array = [random.randint(1, 50) for _ in range(10)]

    print(rand_array)

    quicksort(rand_array, 0, len(rand_array)-1)

    print(rand_array)
    