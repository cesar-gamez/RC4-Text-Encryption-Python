import random
import string

#Random key generation
def generate_key():
    key_length = random.randint(50, 100)
    chars = string.ascii_letters + string.punctuation + string.digits
    key = ''
    for i in range(0, key_length):
        key += random.choice(chars)
    return key

def prepare_key(k):
    return [ord(char) for char in k]

#Encryption process
def KSA(key):
    s = [i for i in range(0, 256)]
    j = 0
    for i in range(0, 255):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def PRGA(s):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]

        yield s[(s[i] + s[j]) % 256]

def RC4_encrypt(key):
    s = KSA(key)
    return PRGA(s)



if __name__ == '__main__':
    plain_text = input('Enter text: ')
    key = generate_key()
    key_list = prepare_key(key)
    key_stream = RC4_encrypt(key_list)

    #XOR bitwise operation
    cypher_text = ''
    for char in plain_text:
        cypher_text += "%02X" % (ord(char) ^ next(key_stream))

    print('Encryption: ' + cypher_text)
    print('Key: ' + key)