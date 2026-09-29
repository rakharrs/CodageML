import random
from math import sqrt

from sardinasPatterson import IsUniquelyDecodable
import csv

columns = [
    'language', 'uniquely_decodable', 'nbr_code', 'avg_length',
    'min_length', 'max_length', 'length_ecartype',
     'consecutive_ones', 'consecutive_zeros',
    'freq_0', 'freq_1', 'freq_p_0', 'freq_p_1',
    'max_same_length',

    # 'begin_1', 'begin_0', 'end_1', 'end_0',

    'freq_0_1', 'freq_0_2', 'freq_0_3', 'freq_0_4', 'freq_0_5',
    'freq_0_6', 'freq_0_7', 'freq_0_8', 'freq_0_9', 'freq_0_10',
    'freq_1_1', 'freq_1_2', 'freq_1_3', 'freq_1_4', 'freq_1_5',
    'freq_1_6', 'freq_1_7', 'freq_1_8', 'freq_1_9', 'freq_1_10',
]


def set_to_string(s):
    """
  Converts a set to a string representation.

  Args:
    s (set): The set to convert.

  Returns:
    str: The string representation of the set.
  """
    s = sorted(s)
    return ','.join(s)


def get_length_ecartype(codes):
    n = len(codes)
    avg_length = get_avg_length(codes)
    return sqrt((sum((len(code) - avg_length) ** 2 for code in codes)) / n)


def string_to_set(data_string):
    """
      Converts a comma-separated string to a set.

      Args:
          data_string: The string containing comma-separated data.

      Returns:
          A set containing the individual elements from the string.
    """
    # Split the string by comma and remove any leading/trailing spaces
    data_list = [item.strip() for item in data_string.split(",")]
    return set(data_list)


def binary_ecartype(codes):
    """
    Calculates the ecartype of 1 and 0 in the codes.
    Args:
        codes (set): The codes.
    """
    n = 2
    string_code = set_to_string(codes).replace(',', '')
    total_1 = 0
    total_0 = 0
    for string in string_code:
        if string == '1':
            total_1 += 1
        else:
            total_0 += 1


def get_frequencies_percent(codes, max_length):
    """
    Args:
        codes (set): set of code (str)
        max_length (int): max length of codes
    Returns:
        list: list of frequencies 0, 1
    """
    frequencies_0 = []
    frequencies_1 = []
    index = 0
    total = len(codes)
    for code in codes:
        frequencies_0.append(count_occurrences(code, '0') / total)
        frequencies_1.append(count_occurrences(code, '1') / total)
        index += 1

    while index < max_length:
        frequencies_0.append(0)
        frequencies_1.append(0)
        index += 1

    return frequencies_0, frequencies_1


def get_frequencies(codes, max_length):
    """
    Args:
        codes (set): set of code (str)
        max_length (int): max length of codes
    Returns:
        list: list of frequencies 0, 1
    """
    frequencies_0 = []
    frequencies_1 = []
    index = 0
    for code in codes:
        frequencies_0.append(count_occurrences(code, '0'))
        frequencies_1.append(count_occurrences(code, '1'))
        index += 1

    while index < max_length:
        frequencies_0.append(0)
        frequencies_1.append(0)
        index += 1

    return frequencies_0, frequencies_1


def get_avg_length(codes):
    """
    Calculates the average length of a code
    Args:
        codes (set): set of codes/words
    Returns:
        float: average length
    """
    avg = 0
    for code in codes:
        avg += len(code)
    # return avg / len(codes)
    return avg / len(codes)


def generate_word():
    """
    Generates a random binary word (str)

    egs:
        - 01
        - 1001
        - 00111...
    Returns:
        str: Random binary word (str)
    """
    val = ''
    word_length = random.randint(1, 7)
    for i in range(word_length):
        val += str(random.randint(0, 1))
    return val


def count_occurrences(word, letter):
    """
    Counts the number of occurrences of a letter 'letter' in a word.

    Args:
        word (str): The word to count occurrences of.
        letter (str): The letter to count occurrences of.

    Returns:
        int: The number of occurrences of the letter in the word.
    """
    return sum([1 for word_letter in word if letter == word_letter])


def generate_language():
    """
    Generates a random language as a set of words (str).
    Returns:
        set: Random language.
    """
    val = set()
    language_length = random.randint(1, 10)
    while len(val) < language_length:
        val.add(generate_word())
    return val


def get_min_length(codes):
    min_length = 0
    for code in codes:
        if len(code) < min_length:
            min_length = len(code)
    return min_length


def get_max_length(codes):
    max_length = 0
    for code in codes:
        if len(code) > max_length:
            max_length = len(code)
    return max_length

def get_max_same_length(codes):
    max = 0
    for code in codes:
        if len(code) > max:
            max += 1
    return max

def generate_model_row(code):
    """
    Generates a model row
    Args:
        code (set): set of codes/words
    Returns:
        list: Random model row
    """
    code_str = set_to_string(code)
    uniquely_decodable = IsUniquelyDecodable(code)
    nbr_code = len(code)
    avg_length = get_avg_length(code)
    min_length = get_min_length(code)
    max_length = get_max_length(code)
    length_ecartype = get_length_ecartype(code)
    freq_0, freq_1 = get_frequencies(code, 10)
    freq_p_0, freq_p_1 = get_frequencies_percent(code, 10)

    freq__0 = sum(freq_0) / len(code)
    freq__1 = sum(freq_1) / len(code)
    code_string = set_to_string(code).replace(',', '')

    freq__p_0 = sum(freq_0) / len(code_string)
    freq__p_1 = sum(freq_1) / len(code_string)
    max_same_length = get_max_same_length(code)

    # tet = code_str.replace(',', '')
    consecutive_zeros, consecutive_ones = count_consecutives_bits_set(code)

    frequencies = freq_0 + freq_1
    frequencies_p = freq_p_0 + freq_p_1
    return [code_str, int(uniquely_decodable), nbr_code, avg_length, min_length, max_length, length_ecartype,
            consecutive_ones, consecutive_zeros,
            freq__0,
            freq__1, freq__p_0, freq__p_1, max_same_length] + frequencies


def generate_model(n):
    data_generated = set()
    with open('data/mydata.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(columns)
        print("Generating model data...")
        is_unique_to_generate = True
        # index = int(100)
        while len(data_generated) < n:

            codes = generate_language()
            if is_unique_to_generate:
                while not IsUniquelyDecodable(codes):
                    codes = generate_language()
                is_unique_to_generate = False
            else:
                while IsUniquelyDecodable(codes):
                    # codes = generate_language()
                    codes = generate_language()
                is_unique_to_generate = True
            print(len(data_generated) + 1, "/", n, "- Generated = ", (len(data_generated) % 9) + 2)

            writer.writerow(generate_model_row(codes))
            data_generated.add(set_to_string(codes))


# print(get_frequencies({'01', '101'}, 10))
# print(columns)
# print(generate_model_row({'01', '101'}))

def generate_redundant_code(element):
    """
    Args:
        element (str): element
    Return
        set: set of codes/words
    """
    val = set()
    language_length = random.randint(2, 5)
    index = 100
    while len(val) < language_length:
        if index < 0:
            break
        index += -1
        word_length = random.randint(1, 5)
        word = ''
        for i in range(word_length):
            word += element
        val.add(word)
    return val


def generate_code(language_length):
    """
    Args:
        word_length (int): word length
    Return
        set: set of codes/words
    """
    val = set()
    while len(val) < language_length:
        val.add(generate_word())
    return val


def generate_data_redundant_code():
    element = random.randint(0, 1)
    return generate_redundant_code(str(element))


def count_consecutive_bits(binary_string):
    """
  Counts the number of consecutive 1s or 0s in a binary string.

  Args:
      binary_string: The string representing the binary number.

  Returns:
      A tuple containing two elements:
          - The count of consecutive 1s.
          - The count of consecutive 0s.
  """
    consecutives_0 = 0
    consecutives_1 = 0
    temp = ''
    for char in binary_string:
        if char == temp:
            if char == '0':
                consecutives_0 += 1
            if char == '1':
                consecutives_1 += 1
        else:
            temp = char
    return consecutives_1, consecutives_0

def count_consecutives_bits_set(setcode):
    consecutive_ones = 0
    consecutive_zeros = 0
    for code in setcode:
        consecutives = count_consecutive_bits(code)
        if len(code) - 1 <= 0:
            consecutive_ones = 0
            consecutive_zeros = 0
        else:
            consecutive_zeros += consecutives[0]
            consecutive_ones += consecutives[1]
    return consecutive_ones, consecutive_zeros

def coun_differences_01(word):
    count = 0
    index = 0
    while index < len(word):
        if int(word[index]) < int(word[index + 1]):
            count += 1
        index += 1
    return count

def coun_differences_10(word):
    count = 0
    index = 0
    while index < len(word):
        if int(word[index]) > int(word[index + 1]):
            count += 1
        index += 1
    return count





# Example usage
# binary_string = "1000"
# consecutive_ones, consecutive_zeros = count_consecutive_bits(binary_string)
# print(consecutive_zeros)
# print(f"Consecutive 1s: {consecutive_ones}, Consecutive 0s: {consecutive_zeros}")
# print(generate_data_redundant_code())

# generate_model(10000)
# print(count_consecutive_bits('00000'))