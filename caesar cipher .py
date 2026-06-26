def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 35:
        return 'Shift must be an integer between 1 and 35.'

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    if not encrypt:
        shift = -shift

    shifted_chars = chars[shift:] + chars[:shift]

    translation_table = str.maketrans(
        chars + chars.upper(),
        shifted_chars + shifted_chars.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Input
plain_text = input("Enter text to encrypt: ")
shift = int(input("Enter key (1-35): "))

encrypted = encrypt(plain_text, shift)
print("Encrypted:", encrypted)

key = int(input("Enter the same key to decrypt: "))
decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
