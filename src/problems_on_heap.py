import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

if __name__ == "__main__":
    arr = [1, 7, 8, 4, 2, 3, 9, 10, 56, 99, 45]
    print(heap_sort(arr))