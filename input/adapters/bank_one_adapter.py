from typing import List

from input.adapters.base_adapter import AbstractAdapter
from settings import DEFAULT_INPUT_LAYOUT


class BankOneTransactionAdapter(AbstractAdapter):
    input_layout = DEFAULT_INPUT_LAYOUT

    def __init__(self, row: List):
        assert len(row) == len(self.input_layout)
        self.row = row

    @classmethod
    def meets_adapter(cls, header: List[str]) -> bool:
        return set(cls.input_layout) == set(header)

    def format_row(self) -> List:
        return [
            self._format_timestamp(),
            self._format_type(),
            self._format_amount(),
            self._format_to(),
            self._format_from()
        ]

    def _format_timestamp(self) -> str:
        return self.row[0]

    def _format_type(self) -> str:
        return self.row[1]

    def _format_amount(self) -> str:
        return self.row[2]

    def _format_to(self) -> str:
        return self.row[3]

    def _format_from(self) -> str:
        return self.row[4]
