def reverse_string():
    input_string = input("Masukkan string (ex: NEGIE1): ")
    
    letters = ''.join(filter(str.isalpha, input_string))
    number = ''.join(filter(str.isdigit, input_string))
    # reversed_string = ''
    # for char in letters:
    #     reversed_string = char + reversed_letters
    reversed_string = letters[::-1] # this have the same outcome like the function above
    result = reversed_string + numbers
    
    print("\n")
    print("Hasil:", result)

