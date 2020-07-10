def has_negatives(a):
    cache = {}

    a.sort(reverse = True)

    for num in a:
        if num > 0:
            cache[num] = 0
        else:
            if num * -1 in cache:
                cache[num * -1] = num
    
    result = [key for key in cache if cache[key] != 0]

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
