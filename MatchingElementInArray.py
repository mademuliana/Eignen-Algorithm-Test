def matching_elements_in_array():
    input_string = input("Masukkan elemen INPUT (pisahkan dengan koma: element1,element2...): ")
    input_array = input_string.split(',')
    
    query_string = input("Masukkan elemen QUERY (pisahkan dengan koma: element1,element2...): ")
    query_array = query_string.split(',')
    
    count = {}
    for word in input_array:
        word = word.strip()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
            
    results = []
    for word in query_array:
        word = word.strip()
        results.append(count.get(word, 0))
    
    print("\n")
    print("OUTPUT =", results)
