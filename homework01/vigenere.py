def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    check = 0
    for i in plaintext:
        if not i.isalpha():
            check += 1
            element_code = ord(i)
        elif i.islower():
            shift = ord(keyword[check % len(keyword)]) - ord("a")
            element_code = (ord(i) + shift - ord("a")) % 26 + ord("a")
            check += 1
        else:
            shift = ord(keyword[check % len(keyword)]) - ord("A")
            element_code = (ord(i) + shift - ord("A")) % 26 + ord("A")
            check += 1
        ciphertext += chr(element_code)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    check = 0
    for i in ciphertext:
        if not i.isalpha():
            check += 1
            element_code = ord(i)
        elif i.islower():
            shift = ord(keyword[check % len(keyword)]) - ord("a")
            element_code = (ord(i) - shift - ord("a")) % 26 + ord("a")
            check += 1
        else:
            shift = ord(keyword[check % len(keyword)]) - ord("A")
            element_code = (ord(i) - shift - ord("A")) % 26 + ord("A")
            check += 1
        plaintext += chr(element_code)
    return plaintext
