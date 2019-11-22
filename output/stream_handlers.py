from abc import ABCMeta, abstractmethod
from typing import TextIO


class AbstractOutputStreamHandler(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        ...


class FileOutputStreamHandler(AbstractOutputStreamHandler):
    def __init__(self, output_resource: str, *args, **kwargs) -> None:
        self.output_resource = output_resource

    def open(self) -> TextIO:
        return open(self.output_resource, 'w')
