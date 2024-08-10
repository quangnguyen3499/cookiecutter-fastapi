import string
from datetime import datetime
from pathlib import Path

from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel
from pydantic import ValidationError

ALPHA_NUM = string.ascii_letters + string.digits


def is_valid_json(model: BaseModel, data: dict) -> bool:
    try:
        model.model_validate(data)
        return True
    except ValidationError:
        return False


def list_files_and_folders(folder_path):
    """Lists all files and folders in the specified folder with timestamps."""
    try:
        path = Path(folder_path)
        if not path.is_dir():
            return []
        files = []
        folders = []
        for entry in path.iterdir():
            timestamp = datetime.fromtimestamp(entry.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            if entry.is_file():
                files.append((entry.name, timestamp))
            elif entry.is_dir():
                folders.append(
                    (f"{entry.name}/", timestamp),
                )  # Append '/' to indicate it's a folder
        # Sort and combine the lists
        return sorted(files, key=lambda x: x[0]) + sorted(folders, key=lambda x: x[0])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def read_yaml_file(file_path):
    """Reads content of a yaml file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
