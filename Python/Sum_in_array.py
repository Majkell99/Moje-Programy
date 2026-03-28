def sum_in_array(array: list, number: int):
    n = len(array)
    results = []

    for i in range(n):
        for j in range(n - i):
            if (array[i] != array[j + i]):
                if ([array[i], array[j + i]] not in results and [array[j + i], array[i]] not in results):
                    if(array[i] + array[j + i] == number):
                        results.append([array[i], array[j + i]])
    
    if (len(results) == 0):
        return "Results not found"
    else:
        m = len(results)
        results_sorted = []
        for i in range(m):
            k = results[i][0]
            p = results[i][1]
            if k > p:
                results_sorted.append([k, p])
            else:
                results_sorted.append([p, k])
            
        for i in range(m):
            maxx = max(results_sorted)
            results_sorted.pop(results_sorted.index(maxx))
            print(maxx)

array = [1, 10, 3, 0, 7, -12, 8, 92, -4, -17, 24, 9, -1, 25, -84]
a = sum_in_array(array, 8)
a
