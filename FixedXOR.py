def fixed_xor(hex_string1, hex_string2):

    # to convert hex strings to bytes
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)

    # to do the XOR operation
    result_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    # to convert the result back to hex
    result_hex = result_bytes.hex()

    return result_hex

# Example String
hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

result = fixed_xor(hex_string1, hex_string2)
print(result)
