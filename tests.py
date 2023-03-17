from math import sqrt, erfc
from scipy.special import gammainc


def frequency_bit_test(subsequence: str) -> float:
    """
    The function performs the frequency bit test for a subsequence of bits.

    :param subsequence: subsequence of bits.
    :return: P_value.
    """
    n = len(subsequence)
    s_n = 0
    for i in subsequence:
        s_n += 1 if i == '1' else -1
    p_value = erfc(1 / sqrt(2 * n) * s_n)
    return p_value


def identical_consecutive_bit_test(subsequence: str) -> float:
    """
    The function performs the test for identical consecutive bits for a subsequence of bits.

    :param subsequence: subsequence of bits.
    :return: P_value.
    """
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


def longest_sequence_of_ones_test(subsequence: str) -> float:
    """
    The function performs the test for the longest sequence of ones in a unit for a subsequence of bits.

    :param subsequence: subsequence of bits.
    :return: P_value.
    """
    n = len(subsequence)
    units = [0] * (n // 8)
    for i in range(len(units)):
        cur_one_sequence = 0
        for j in range(8):
            if subsequence[i * 8 + j] == '1':
                cur_one_sequence += 1
            else:
                if units[i] < cur_one_sequence:
                    units[i] = cur_one_sequence
                cur_one_sequence = 0
        if units[i] < cur_one_sequence:
            units[i] = cur_one_sequence
    v = [units.count(0) + units.count(1), units.count(2), units.count(3),
         len(units) - units.count(0) - units.count(1) - units.count(2) - units.count(3)]
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    x_2 = 0
    for i in range(4):
        x_2 += ((v[i] - 16 * pi[i]) ** 2) / (16 * pi[i])
    p_value = gammainc(1.5, x_2 / 2)
    return p_value


if __name__ == '__main__':
    with open('subsequence.txt', 'r', encoding='utf-8') as f:
        bit_row = f.read()
    print(f'Последовательность:\n{bit_row}')
    print(f'\nЧастотный побитовый тест: {frequency_bit_test(bit_row)}')
    print(f'Тест на одинаковые подряд идущие биты: {identical_consecutive_bit_test(bit_row)}')
    print(f'Тест на самую длинную последовательность единиц в блоке: {longest_sequence_of_ones_test(bit_row)}')

# subsequences:
# 11001001111101110011001000000100110110001110011010000011011011101110010011101011011100011000010110010010101000111110110010001010
# 11001101011110101010010110100101011100001110100001000011110110110110110101010000010010011001110111000001100010110100011001000111
# 10010110000110111001111111011001010111000110111011001111001010011110001010010000010100000111001011100110001111110010101010100111
