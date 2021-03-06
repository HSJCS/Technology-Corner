
def tim_sort(arr):
    
    run_min = 32
    n = len(arr)
    
    for i in range(0, n, run_min):
        insertion_sort(arr, i, min((i + run_min - 1), n - 1))

    length = run_min
    
    while length < n:
        for begin in range(0, n, length * 2):
            
            mid = begin + length - 1
            end = min((begin + length * 2 - 1), (n-1))

            array_merged = merge(left=array[begin:mid + 1], right=array[mid + 1:end + 1])
            array[begin:begin + len(array_merged)] = array_merged

        length *= 2

    return arr