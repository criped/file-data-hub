from typing import List

from input.adapters.base_adapter import AbstractAdapter, NullAdapter


class InputManager:
    def __init__(self, input_layout: List[str]):
        self.input_layout = input_layout

    def identify_adapter(self) -> type(AbstractAdapter):
        for adapter_class in AbstractAdapter.__subclasses__():
            if adapter_class.meets_adapter(self.input_layout):
                return adapter_class
        return NullAdapter
