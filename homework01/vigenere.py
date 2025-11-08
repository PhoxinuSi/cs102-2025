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
    ciphertext = ""
    a_ord = ord("a")
    big_a_ord = ord("A")
    delta_english = ord("Z") - ord("A") + 1
    for index, letter in enumerate(plaintext):
        if "a" <= letter <= "z" or "A" <= letter <= "Z":
            register = a_ord if letter.islower() else big_a_ord
            shift = ord(keyword[index % len(keyword)]) - register
            element_code = (ord(letter) + shift - register) % delta_english + register
            ciphertext += chr(element_code)
        else:
            ciphertext += letter
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
    a_ord = ord("a")
    big_a_ord = ord("A")
    delta_english = ord("Z") - ord("A") + 1
    for index, letter in enumerate(ciphertext):
        if "a" <= letter <= "z" or "A" <= letter <= "Z":
            register = a_ord if letter.islower() else big_a_ord
            shift = ord(keyword[index % len(keyword)]) - register
            element_code = (ord(letter) - shift - register) % delta_english + register
            plaintext += chr(element_code)
        else:
            plaintext += letter
    return plaintext
