def check_key(input_message, key):
    if len(input_message) == len(key):
        return key
    for i in range(len(input_message) - len(key)):
        key += key[i % len(key)]
    return key


# encryption vvv


def encrypt_vigenere(input_message, key):
    if not check_case(input_message, key):
        return 'Enter the message and the key using only upper case'
    key = check_key(input_message, key)
    output = ''
    for i in range(len(input_message)):
        if input_message[i] == ' ':
            output += ' '
            continue
        temp = (ord(input_message[i]) + ord(key[i])) % 26
        temp += ord('A')
        output += chr(temp)
    return output


# decryption vvv


def decrypt_vigenere(input_message, key):
    if not check_case(input_message, key):
        return 'Enter the message and the key using only upper case'
    key = check_key(input_message, key)
    output = ''
    for i in range(len(input_message)):
        if input_message[i] == ' ':
            output += ' '
            continue
        temp = (ord(input_message[i]) - ord(key[i]) + 26) % 26
        temp += ord('A')
        output += chr(temp)
    return output


def check_case(input_message, key):
    for i in range(len(input_message)):
        if input_message[i].islower():
            return False
    for i in range(len(key)):
        if input_message[i].islower():
            return False
    return True


print(encrypt_vigenere('HELLO THERE', 'DISTLAB'))
print(decrypt_vigenere('KMDEZ UKMJX', 'DISTLAB'))





