# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV
# The quick brown fox jumped over the lazy sleeping dog
# shift 11

# encrypt('123345', 1) -> '23456'

def encrypt(plain, key):
    encrypted_text = ''
    # for loop
    for char in plain:
        # print(char)
        temp = int(char)
        # print(temp)
        # while temp > 9:
        #     temp -= 10
        temp2 = (temp + key) %10
        encrypted_text += str(temp2)
    return encrypted_text    


def decrypt(encoded, key):
    # 8901, 3 -> 5678
    # decrypt_text = ''
    # for char in encoded:
    decrypted_text = encrypt(encoded, -key)
    return decrypted_text


if __name__=="__main__":
    # print(encrypt('12345', 1))
    # print(encrypt('678', 1))
    # print(encrypt('5678', 5)) # 0123
    # plain = '1234'
    # key = 82374
    # try1 = encrypt(plain, key) # 5678
    # print(try1)
    # try2 = decrypt(try1, key)
    # print(try2)

    check_word = 'pieeeee'
    check_word2 = 'cat'
    # pda (3)
    # rfc (5)

    import nltk

    nltk.download('words', quiet=True)

    from nltk.corpus import words
    
    word_list = words.words()
    # print(word_list)

    if check_word2 in word_list:
        print('Yep, its here')
    else:
        print('nope')
