def bitwise_and(a, b):
    result = 0
    position = 1
    while a > 0 or b > 0:
        a_bit = a % 2
        b_bit = b % 2
        if a_bit == 1 and b_bit == 1:
            result += position
        a //= 2
        b //= 2
        position *= 2
    return result

def bitwise_xor(a, b):
    result = 0
    position = 1
    while a > 0 or b > 0:
        a_bit = a % 2
        b_bit = b % 2
        if a_bit != b_bit:
            result += position
        a //= 2
        b //= 2
        position *= 2
    return result

# Take user input
s = input("Enter a string: ")

print("\nCharacter | ASCII Value | AND with 127 | XOR with 127")
print("---------------------------------------------------------")
for ch in s:
    ascii_val = ord(ch)
    and_result = bitwise_and(ascii_val, 127)
    xor_result = bitwise_xor(ascii_val, 127)
    print(f"{repr(ch):9} | {ascii_val:12} | {and_result:13} | {xor_result:13}")

