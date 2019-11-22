from abc import ABCMeta, abstractmethod
from typing import List


class AbstractAdapter(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def meets_adapter(cls, header: List[str]) -> bool:
        ...

    @abstractmethod
    def format_row(self) -> bool:
        ...


class NullAdapter(AbstractAdapter):
    input_layout = None

    @classmethod
    def meets_adapter(cls, header: List[str]) -> bool:
        return False

    def format_row(self) -> List:
        return []
