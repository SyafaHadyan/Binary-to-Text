def binary_to_text(binary_string):
    decimal_num = int(binary_string, 2)
    text = chr(decimal_num)
    return text

binary_str = "01110110"
text = binary_to_text(binary_str)
print(text)
