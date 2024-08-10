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


def format_csv_to_openai_training_data(csv_path, system_message, output_path):
    df = pd.read_csv(csv_path)
    df.replace(np.nan, None, inplace=True)

    # Get the column names for user and assistant messages
    user_column = df.columns[2]
    assistant_column = df.columns[5]

    with open(output_path, "w") as f:
        # Loop through each row and create a separate "messages" structure for each
        for _, row in tqdm(df.iterrows()):
            user_msg = row[user_column]
            assistant_msg = row[assistant_column]

            if not user_msg or not assistant_msg:
                continue

            message_structure = {
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": assistant_msg},
                ],
            }

            f.write(json.dumps(message_structure) + "\n")
