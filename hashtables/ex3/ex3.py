def intersection(arrays):
    cache = {}

    for i in range(len(arrays[0])):
        cache[arrays[0][i]] = 1
    
    for arr in range(1, len(arrays)):
        array_num = arrays[arr]

        for i in range(len(array_num)):
            if array_num[i] in cache:
                cache[array_num[i]] += 1

    result = [key for key in cache if cache[key] == len(arrays)]

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))