def single_byte_xor_cipher(hex_string, key):
    decoded_bytes = bytes.fromhex(hex_string)
    decrypted_text = ''.join(chr(byte ^ key) for byte in decoded_bytes)
    return decrypted_text

def score_plaintext(plaintext):
    # scoring mechanism
    english_letter_frequency = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
        'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
        'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
        's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
        'y': 1.974, 'z': 0.074
    }

    score = sum(english_letter_frequency.get(char, 0) for char in plaintext.lower())
    return score

def find_xor_key(hex_string):
    best_score = 0
    best_key = 0
    for key in range(256):  # All possible ASCII characters as keys
        decrypted_text = single_byte_xor_cipher(hex_string, key)
        current_score = score_plaintext(decrypted_text)
        if current_score > best_score:
            best_score = current_score
            best_key = key
    return best_key

# Example with the provided hex string
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
best_key = find_xor_key(hex_string)
decrypted_message = single_byte_xor_cipher(hex_string, best_key)

print("Best Key:", best_key)
print("Decrypted Message:", decrypted_message)
