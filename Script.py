def bits_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

input_bits = input("Enter binary code: ")
output_text = bits_to_text(input_bits)
print("Text equivalent:", output_text)
