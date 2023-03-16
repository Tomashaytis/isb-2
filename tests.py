from math import sqrt, erfc


def frequency_bit_test(subsequence: str) -> float:
    n = len(subsequence)
    s_n = 0
    for i in subsequence:
        s_n += 1 if i == '1' else -1
    p_value = erfc(1 / sqrt(2 * n) * s_n)
    return p_value


if __name__ == '__main__':
    with open('subsequence.txt', 'r', encoding='utf-8') as f:
        bit_row = f.read()
    print(frequency_bit_test(bit_row))

# 11001001111101110011001000000100110110001110011010000011011011101110010011101011011100011000010110010010101000111110110010001010
