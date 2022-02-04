# Following function implements encryption with Vigenere Cypher

def encrypt_vigenere(input_message, key):
    return ""


def check_key(input_message, key):
    if len(input_message) == len(key):
        return key
    for i in range(len(input_message) - len(key)):
        key += key[i % len(key)]
    return key


print(check_key('abcdefgh', 'distlab'))
