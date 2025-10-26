def shift_character(character: str, offset: int) -> str:
    return chr((ord(character) + offset) % (1 << 8))


def caesar_encrypt(clear_text: str, offset: int) -> str:
    return "".join([shift_character(character, offset) for character in clear_text])


def caesar_decrypt(clear_text: str, offset: int) -> str:
    return "".join([shift_character(character, -offset) for character in clear_text])


key: int = 1
encrypted_message = caesar_encrypt("THE QUICK BROWN fox JUMPS OVER THE LAZY DOG", key)
decrypted_message = caesar_decrypt(encrypted_message, key)

print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
