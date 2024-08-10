from abc import ABC
from abc import abstractmethod


class Generator(ABC):
    """Class to generate string from .yaml files"""

    @abstractmethod
    def generate(self):
        """Return string format from given .yaml file"""
