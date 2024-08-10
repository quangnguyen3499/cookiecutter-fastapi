from typing import List
from typing import Optional

from langchain.pydantic_v1 import BaseModel
from langchain.pydantic_v1 import Field


class ExampleModel(BaseModel):
    names: Optional[List[str]] = Field(
        [],
        description="The list of name of the expert that user wants to book",
    )
