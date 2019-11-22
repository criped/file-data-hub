from input.adapters import BankOneTransactionAdapter
from settings import DEFAULT_INPUT_LAYOUT


class BankOneTransactionAdapterTest:
    row_test = [
        'Oct 1 2019',
        'remove',
        '99.10',
        '182',
        '198'
    ]

    adapter_instance = BankOneTransactionAdapter(row_test)

    def test_meets_adapter(self):
        assert BankOneTransactionAdapter.meets_adapter(DEFAULT_INPUT_LAYOUT) is True

    def test_format_row(self):
        BankOneTransactionAdapter()
        assert self.adapter_instance.format_row() == self.row_test
