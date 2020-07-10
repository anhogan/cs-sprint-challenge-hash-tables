def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for i in range(length):
        current = weights[i]
        remaining = limit - current

        if remaining in cache:
            if cache[remaining] > i:
                return[cache[remaining], i]
            else:
                return [i, cache[remaining]]
        else:
            cache[current] = i

    return None
