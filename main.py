def check_key(input_message, key):
    if len(input_message) == len(key):
        return key
    for i in range(len(input_message) - len(key)):
        key += key[i % len(key)]
    return key


# encryption vvv


def encrypt_vigenere(input_message, key):
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


print(encrypt_vigenere('HELLO THERE', 'DISTLAB'))




