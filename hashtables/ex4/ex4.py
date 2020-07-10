def has_negatives(a):
    cache = {}
    result = []

    a.sort(reverse = True)

    for num in a:
        if num > 0:
            cache[num] = 0
        else:
            if num * -1 in cache:
                cache[num * -1] = num
    
    filtered_cache = [(key, cache[key]) for key in cache if cache[key] != 0]
    
    for key, value in filtered_cache:
        result.append(key)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
