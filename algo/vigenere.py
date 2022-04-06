def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def cipherText(string, keyword):
    cipher_text = []
    key = generateKey(string, keyword)
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def originalText(cipher_text, keyword):
    orig_text = []
    key = generateKey(cipher_text, keyword)
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) % 26)
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


if __name__ == "__main__":
    string = "geeksforgeeks"
    keyword = "AYUSH"
    
    cipher_text = cipherText(string, keyword)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
          originalText(cipher_text, keyword))
