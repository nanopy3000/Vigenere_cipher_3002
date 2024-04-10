ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(ciphertext, key):
    message_toghether = ''.join(ciphertext.split())
    phrase = ciphertext.split()
    plaintext = ''
    ciphertext_letter = ''
    next = 0
    aggregate = 0
    large_plaintext = len(phrase[0])
    
    
    for i in range(len(message_toghether)):
        p = ALPHABET.index(message_toghether[i])
        n = i % len(key)
        k = ALPHABET.index(key[n])
        c = (p - k) % 26
        ciphertext_letter += ALPHABET[c]
        
        
        if len(ciphertext_letter) == large_plaintext  :
            next += 1
            while next < len(phrase) :   
                large_plaintext += len(phrase[next])
                plaintext += ciphertext_letter[aggregate:len(ciphertext_letter)] + ' '
                aggregate += len(phrase[next-1])
                break
            if next == len(phrase):
                plaintext += ciphertext_letter[aggregate:len(ciphertext_letter)]
    
    return plaintext

message = "TPKGS SJJETJ IAV FNZKZ"

keyword = "BAGGINS"

message_decrypt = decrypt(message, keyword)

print("\n DECRYPT MESSAGE = {} \n".format(message_decrypt))
