import csv
from pathlib import Path

from input.managers import InputManager
from settings import OUTPUTS, DEFAULT_INPUT_LAYOUT, INPUT_FILES_PATH


def write_file_data_into_output(input_file_path, writer_instance):
    with open(input_file_path, 'r') as input_file:
        file_reader = csv.reader(input_file)
        header = file_reader.__next__()
        input_adapter = InputManager(header).identify_adapter()
        for row in file_reader:
            if len(row) == len(input_adapter.input_layout):
                formatted_row = input_adapter(row).format_row()
                writer_instance.write_row(formatted_row)


if __name__ == '__main__':
    for output in OUTPUTS:
        writer_class = output[0]
        for output_resource in output[1]:
            with writer_class.output_stream_handler_class(output_resource).open() as output_stream:
                writer = writer_class(output_stream)
                writer.write_row(DEFAULT_INPUT_LAYOUT)
                files_in_input_path = Path(INPUT_FILES_PATH).iterdir()
                for item in files_in_input_path:
                    if item.is_file():
                        write_file_data_into_output(item, writer)
