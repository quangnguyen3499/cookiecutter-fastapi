import json

import numpy as np
import pandas as pd
import tiktoken
from tqdm import tqdm

encoding = tiktoken.get_encoding("cl100k_base")


def num_tokens_from_string(string: str, model_name: str = "gpt-3.5-turbo-1106") -> int:
    """
    Returns the number of tokens in a text string based on the specified model's encoding.

    Args:
    string (str): The text string to encode.
    model_name (str): The model name to select the encoding. Defaults to 'gpt-3.5-turbo'.

    Returns:
    int: The number of tokens in the encoded string.
    """

    # Obtain the encoding for the specified model
    encoding = tiktoken.encoding_for_model(model_name)

    # Return the number of tokens in the encoded string
    return len(encoding.encode(string))
