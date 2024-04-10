ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, key):
    message_toghether = ''.join(message.split())
    phrase = message.split()
    ciphertext = ''
    ciphertext_letter = ''
    next = 0
    aggregate = 0
    large_plaintext = len(phrase[0])
    
    
    for i in range(len(message_toghether)):
        p = ALPHABET.index(message_toghether[i])
        n = i % len(key)
        k = ALPHABET.index(key[n])
        c = (p + k) % 26
        ciphertext_letter += ALPHABET[c]
        
        
        if len(ciphertext_letter) == large_plaintext  :
            next += 1
            while next < len(phrase) :   
                large_plaintext += len(phrase[next])
                ciphertext += ciphertext_letter[aggregate:len(ciphertext_letter)] + ' '
                aggregate += len(phrase[next-1])
                break
            if next == len(phrase):
                ciphertext += ciphertext_letter[aggregate:len(ciphertext_letter)]
    
    return ciphertext

message = "SPEAK FRIEND AND ENTER"

keyword = "BAGGINS"

message_encrypt = encrypt(message, keyword)

print("\n ENCRYPT MESSAGE = {} \n".format(message_encrypt))
