def encrypt_poly_shift(plaintext: str, odd_shift: int, even_shift: int) -> str:
    ciphertext = ""
    a_ord = ord("а")
    big_a_ord = ord("А")
    russian_delta = ord("Я") - ord("А") + 1
    for index, elem in enumerate(plaintext):
        if "a" <= elem <= "я" or "А" <= elem <= "Я":
            register = a_ord if elem.islower() else big_a_ord
            shift = odd_shift if index % 2 == 1 else even_shift
            element_code = (ord(elem) + shift - register) % russian_delta + register
            ciphertext += chr(element_code)
        else:
            ciphertext += elem
    return ciphertext
