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
    a_ord = ord("a")
    big_a_ord = ord("A")
    delta_english = ord("Z") - ord("A") + 1
    for i in plaintext:
        if not i.isalpha():
            element_code = ord(i)
        else:
            register = a_ord if i.islower() else big_a_ord
            element_code = (ord(i) + shift - register) % delta_english + register
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
    a_ord = ord("a")
    big_a_ord = ord("A")
    delta_english = ord("Z") - ord("A") + 1
    plaintext = ""
    for i in ciphertext:
        if not i.isalpha():
            element_code = ord(i)
        else:
            register = a_ord if i.islower() else big_a_ord
            element_code = register + (ord(i) - shift - register) % delta_english
        plaintext += chr(element_code)
    return plaintext
