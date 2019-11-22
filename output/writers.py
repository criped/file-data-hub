import csv
from abc import ABCMeta, abstractmethod
from typing import TextIO, List

from output.stream_handlers import FileOutputStreamHandler


class BaseWriter(metaclass=ABCMeta):
    output_stream_handler_class = None

    @abstractmethod
    def write_row(self, *args, **kwargs) -> None:
        ...


class CSVFileWriter(BaseWriter):
    output_stream_handler_class = FileOutputStreamHandler

    def __init__(self, file: TextIO):
        self.writer = csv.writer(file, delimiter=',')

    def write_row(self, row: List, *args, **kwargs) -> None:
        self.writer.writerow(row)
