import os
from pathlib import Path


# API
VERSION = "v1"
API_PREFIX = f"/api/{VERSION}"

DB_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration
CONFIG_PATH = os.path.join(BASE_DIR, "configs.ini")

# OpenAI
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo-1106"
DEFAULT_OPENAI_REQUEST_TIMEOUT = 25

# -------------------------------- Chatbot Response --------------------------------
ERROR_RESPONSE = (
    "We're undergoing maintenance to improve our services. "
    "Please bear with us and return after some minutes. Thanks for your understanding"
)

ERROR_TIMEOUT_RESPONSE = (
    "I apologize for the inconvenience. To proceed smoothly, please click 'Re-generate' button "
    "or consider making your question/request shorter. Thank you for your patience!"
)

# Default Chatbot Message Reponses
NO_FOUND_SEARCH_EXPERT_RESPONSE = (
    "It seems the results don't quite match what you need. "
    "Mind tweaking your search a bit? "
    "That way, we can find the perfect fit for you"
)

DEFAULT_START_MSG = "Here are some recommended experts:"
DEFAULT_END_MSG = [
    "Do you want to find more about them? I can also look for other options if you prefer?",  # noqa
    "Do these results meet your requirements? If not, I can search for alternative specialists tailored to your needs.",  # noqa
    "Would you like to learn more about them, or would you prefer I explore other alternatives?",  # noqa
    "Would you like more details on these options, or should I continue searching for other possibilities that might suit you better?",  # noqa
]


DEFAULT_REQUEST_MORE_START_MSG = (
    "Based on what you're looking for, here are a few more recommendations:"
)
DEFAULT_REQUEST_MORE_END_MSG = "Do you have a specific expert in mind, or would you like me to suggest some other experts we've got on hand?"  # noqa
LOW_BUDGET_MSG = "Unfortunately, we don't have anyone in that budget range. However, I can recommend some suggestions with slightly higher rates. "  # noqa

REQUEST_MORE_MESSAGE = "It seems like finding the right expert has been a bit of a challenge. To streamline the process, could you please consider making a few adjustments to your search criteria?"  # noqa
UPDATE_KEYWORDS_MESSAGE = "Even with keyword tweaks, finding the right expert is proving challenging. How about we opt for personalized assistance? Share your email and phone, and we'll tailor the search just for you."  # noqa

UNRELATED_MESSAGE_RESPONSE = "The message sounds unrelated to our current discussion. If you have specific questions or requests about finding an expert, please share, and I'll be happy to help."  # noqa

# -------------------------------- Chatbot Response --------------------------------
