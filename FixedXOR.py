def fixed_xor_with_string(hex_str):
    # The fixed string to XOR against
    fixed_xor_string = "686974207468652062756c6c277320657965"

    # Convert hex string to bytes
    bytes1 = bytes.fromhex(hex_str)
    bytes2 = bytes.fromhex(fixed_xor_string)

    # Perform XOR operation
    result_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    # Convert the result back to hex
    result_hex = result_bytes.hex()

    return result_hex

# Example usage with the provided string
input_string = "1c0111001f010100061a024b53535009181c"
result = fixed_xor_with_string(input_string)
print(result)
