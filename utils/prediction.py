import joblib
import pandas as pd
import numpy as np  # type: ignore
from modelGeneration import generate_model_row
from sardinasPatterson import IsUniquelyDecodable


def load_model():
    return joblib.load('/Users/rakharrs/Developer/codage_TSINJO/CodageML/utils/data/test_model4.pkl')


model = load_model()

columns = [
    'language', 'uniquely_decodable', 'nbr_code', 'avg_length',
    'min_length', 'max_length', 'length_ecartype',
    'consecutive_ones', 'consecutive_zeros',
    'freq_0', 'freq_1', 'freq_p_0', 'freq_p_1',
    'max_same_length',

    'freq_0_1', 'freq_0_2', 'freq_0_3', 'freq_0_4', 'freq_0_5',
    'freq_0_6', 'freq_0_7', 'freq_0_8', 'freq_0_9', 'freq_0_10',
    'freq_1_1', 'freq_1_2', 'freq_1_3', 'freq_1_4', 'freq_1_5',
    'freq_1_6', 'freq_1_7', 'freq_1_8', 'freq_1_9', 'freq_1_10',
]


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


def predict(code):
    """
    Args:
        Code (string): Code to be predicted
    Return:
        prediction (boolean): True or False
    """
    set_code = string_to_set(code)
    print(set_code)
    b = pd.DataFrame([generate_model_row(set_code)], columns=columns)

    b.pop('language')
    b.pop('uniquely_decodable')

    b.pop('nbr_code')

    # b.pop('freq_p_0')
    # b.pop('freq_p_1')
    b.pop('freq_0')
    b.pop('freq_1')

    b.pop('consecutive_ones')
    b.pop('consecutive_zeros')

    sardinasPatterson = IsUniquelyDecodable(set_code)
    prediction = bool(model.predict(b)[0])
    return {'code': code, 'sardinas_patterson': sardinasPatterson, 'prediction': prediction}
