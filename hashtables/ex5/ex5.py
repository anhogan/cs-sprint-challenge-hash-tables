# Need to optimize for large test - passes small test

def finder(files, queries):
    file_cache = {}

    for file in files:
        file_cache[file] = []
    
    keys = list(file_cache.keys())

    for query in queries:
        for key in keys:
            if query in key:
                file_cache[key].append(query)

    result = [key for key in file_cache if len(file_cache[key]) > 0]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
