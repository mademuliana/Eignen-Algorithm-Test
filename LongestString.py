def longest_string():
    string = input("Masukkan kalimat: ")
    sentence = string.split()
    
    longest_str = ''
    for word in sentence:
        if len(word) > len(longest_str):
            longest_str = word

    print("\n")
    print("Kata terpanjang:", longest_str)
