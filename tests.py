from math import sqrt, erfc


def frequency_bit_test(subsequence: str) -> float:
    n = len(subsequence)
    s_n = 0
    for i in subsequence:
        s_n += 1 if i == '1' else -1
    p_value = erfc(1 / sqrt(2 * n) * s_n)
    return p_value


def identical_consecutive_bit_test(subsequence: str):
    n = len(subsequence)
    s = 0
    for i in subsequence:
        s += 1 if i == '1' else 0
    s = s / n
    p_value = 0
    if abs(s - 0.5) < 1 / sqrt(n):
        v_n = 0
        for i in range(n - 1):
            if subsequence[i] != subsequence[i + 1]:
                v_n += 1
        p_value = erfc(abs(v_n - 2*n*s*(1 - s)) / (sqrt(8 * n) * s * (1 - s)))
    return p_value


if __name__ == '__main__':
    with open('subsequence.txt', 'r', encoding='utf-8') as f:
        bit_row = f.read()
    print(f'Последовательность:\n{bit_row}')
    print(f'\nЧастотный побитовый тест: {frequency_bit_test(bit_row)}')
    print(f'Тест на одинаковые подряд идущие биты: {identical_consecutive_bit_test(bit_row)}')

# 11001001111101110011001000000100110110001110011010000011011011101110010011101011011100011000010110010010101000111110110010001010
# 11001101011110101010010110100101011100001110100001000011110110110110110101010000010010011001110111000001100010110100011001000111
