from collections import Counter
import string

# Function to score plaintext based on character frequency
def score_plaintext(plaintext):
    # Define expected character frequencies in English text
    expected_freq = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
        'z': 0.00074, ' ': 0.13000  # Considering space as the most frequent character
    }
    
    # Count the occurrences of each character in the plaintext
    plaintext_freq = Counter(plaintext.lower())
    
    # Calculate the score based on the absolute difference between actual and expected frequencies
    score = sum(abs(plaintext_freq.get(char, 0) / (len(plaintext) + 1e-6) - expected_freq.get(char, 0)) for char in string.ascii_lowercase + ' ')
    return score

# Function to decrypt the message using single-byte XOR
def decrypt_single_byte_xor(hex_string):
    # Convert hex string to bytes
    ciphertext = bytes.fromhex(hex_string)
    
    best_score = float('inf')
    best_plaintext = ''
    best_key = None
    
    # Iterate through all possible single-byte keys
    for key in range(256):
        plaintext = bytes([byte ^ key for byte in ciphertext]).decode('utf-8', errors='ignore')
        score = score_plaintext(plaintext)
        if score < best_score:
            best_score = score
            best_plaintext = plaintext
            best_key = key
    
    return best_key, best_plaintext

# Hex encoded string
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Decrypt the message
best_key, decrypted_message = decrypt_single_byte_xor(hex_string)

# Print the result
print("Best Key:", best_key)
print("Decrypted Message:", decrypted_message)
