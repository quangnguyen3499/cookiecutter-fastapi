import re
from typing import List


def extract_phone_and_email(text: str):
    # Regex pattern for phone numbers
    phone_pattern = re.compile(
        r"""
        (\+\d{1,3}\s?\d{1,4}\s?\d{1,4}\s?\d{1,4}) |  # International format
        (\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}) |      # Digits with separators
        (\d{7,15}) |                                 # Continuous string of digits
        (0\d{2}\s?\d{3}\s?\d{4}) |                   # UK landline format, e.g., 01234 567 890
        (0\d{3}\s?\d{3}\s?\d{4}) |                   # UK landline alternate format, e.g., 0123 456 789
        (07\d{3}\s?\d{6})                            # UK mobile format, e.g., 07123 456789
        """,
        re.VERBOSE,
    )

    # Regex pattern for email addresses
    email_pattern = re.compile(
        r"\b[A-Za-z0-9._%+-]+(?<!-)@"  # User name part of the email
        r"(?:[A-Za-z0-9-]+(?<!-)\.)+"  # Domain part before the TLD
        r"[A-Za-z]{2,}\b",  # TLD part, allowing only letters and at least two characters
    )

    # Find all matches in the text
    phones = phone_pattern.findall(text)
    emails = re.findall(email_pattern, text)

    # Flatten the tuple results from phone numbers and remove empty strings
    phone_numbers = [num for sublist in phones for num in sublist if num]

    return {"emails": emails, "phone_numbers": phone_numbers}


def replace_content_between_tags(
    text: str,
    start_tag: str,
    end_tag: str,
    replacement_text: str,
) -> str:
    """
    Replace the content between specified start and end tags in the given text with the provided replacement text.

    Args:
    text (str): The original text where the replacement needs to be done.
    start_tag (str): The starting tag to identify the beginning of the content to be replaced.
    end_tag (str): The ending tag to identify the end of the content to be replaced.
    replacement_text (str): The text to replace the content between the start and end tags.

    Returns:
    str: The text with the specified content replaced by the replacement text.
    """
    # Regular expression pattern to match content between the specified tags (including the tags)
    pattern = rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}"

    # Using re.sub to replace the matched content with the replacement text
    replaced_text = re.sub(pattern, replacement_text, text, flags=re.DOTALL)

    return replaced_text


def split_message_around_suggestions(text: str, start_tag: str, end_tag: str) -> List[str]:
    """
    Splits the text into two parts: before 'start_tag' and after 'end_tag'.

    Args:
        text (str): The input text containing the special markers.
        start_tag (str): The starting tag to identify the beginning of the content to be replaced.
        end_tag (str): The ending tag to identify the end of the content to be replaced.

    Returns:
        list: A list containing two strings, the text before 'start_tag' and the text after 'end_tag'.
    """

    # Regular expression pattern to find the text before and after the markers
    pattern = rf"(.*?){start_tag}.*?{end_tag}(.*)"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        # Extract the text before and after the markers, stripping any whitespace
        before_start = match.group(1).strip()
        after_end = match.group(2).strip()
        return [before_start, after_end]
    else:
        # Return the original text in a list if the pattern is not found
        return [text]
