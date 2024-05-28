import random
from math import sqrt

from sardinasPatterson import IsUniquelyDecodable
import csv

columns = [
    'language', 'uniquely_decodable', 'nbr_code', 'avg_length',
    'min_length', 'max_length', 'length_ecartype',
    'freq_0', 'freq_1', 'freq_p_0', 'freq_p_1',
    'freq_p_0_1', 'freq_p_0_2', 'freq_p_0_3', 'freq_p_0_4', 'freq_p_0_5',
    'freq_p_0_6', 'freq_p_0_7', 'freq_p_0_8', 'freq_p_0_9', 'freq_p_0_10',
    'freq_p_1_1', 'freq_p_1_2', 'freq_p_1_3', 'freq_p_1_4', 'freq_p_1_5',
    'freq_p_1_6', 'freq_p_1_7', 'freq_p_1_8', 'freq_p_1_9', 'freq_p_1_10',

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
    total = 0
    total_0 = 0
    total_1 = 0
    for code in codes:
        total += 1
        # total_0 += count_occurrences(code, '0')
        # total_1 += count_occurrences(code, '1')
    for code in codes:
        if total_0 == 0:
            frequencies_0.append(0)
        else:
            frequencies_0.append(count_occurrences(code, '0') * 10 / total)
        if total_1 == 0:
            frequencies_1.append(0)
        else:
            frequencies_1.append(count_occurrences(code, '1') * 10 / total)
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
    return avg / 7


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
    language_length = random.randint(2, 10)
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
    freq__p_0 = sum(freq_p_0) / len(code)
    freq__p_1 = sum(freq_p_1) / len(code)

    frequencies = freq_0 + freq_1
    frequencies_p = freq_p_0 + freq_p_1
    return [code_str, int(uniquely_decodable), nbr_code, avg_length, min_length, max_length, length_ecartype, freq__0,
            freq__1, freq__p_0, freq__p_1] + frequencies_p + frequencies


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
            print(len(data_generated) + 1, "/", n, "- Generated = ", (len(data_generated) % 9)+2)

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


generate_model(10000)
# print(generate_data_redundant_code())
