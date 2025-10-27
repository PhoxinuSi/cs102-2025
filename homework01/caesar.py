def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if not i.isalpha():
            element_code = ord(i)
        else:
            if i.islower():
                element_code = (ord(i) + shift - ord("a")) % 26 + ord("a")
            else:
                element_code = (ord(i) + shift - ord("A")) % 26 + ord("A")
        ciphertext += chr(element_code)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if not i.isalpha():
            element_code = ord(i)
        else:
            if i.islower():
                element_code = ord("a") + (ord(i) - shift - ord("a")) % 26
            else:
                element_code = ord("A") + (ord(i) - shift - ord("A")) % 26
        plaintext += chr(element_code)
    return plaintext
