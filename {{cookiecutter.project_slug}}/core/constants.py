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

# -------------------------------- Chatbot Response --------------------------------
ERROR_RESPONSE = (
    "There's something wrong"
)

ERROR_TIMEOUT_RESPONSE = (
    "Timeout error"
)
