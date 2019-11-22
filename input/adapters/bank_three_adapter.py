import datetime
from typing import List

from input.adapters.base_adapter import AbstractAdapter
from settings import DEFAULT_TIMESTAMP_FORMAT


class BankThreeTransactionAdapter(AbstractAdapter):
    input_layout = ('date_readable', 'type', 'euro', 'cents', 'to', 'from')
    timestamp_format = '%d %b %Y'

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
        return datetime.datetime.strptime(self.row[0], self.timestamp_format).strftime(DEFAULT_TIMESTAMP_FORMAT)

    def _format_type(self) -> str:
        return self.row[1]

    def _format_amount(self) -> str:
        return f"{self.row[2]}.{self.row[3]}"

    def _format_to(self) -> str:
        return self.row[4]

    def _format_from(self) -> str:
        return self.row[5]
