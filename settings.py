from output.writers import CSVFileWriter

OUTPUT_RESOURCE_ID = 'output.txt'
OUTPUT_WRITER = CSVFileWriter
OUTPUTS = (
    (
        OUTPUT_WRITER, (OUTPUT_RESOURCE_ID,)
    ),
)

DEFAULT_INPUT_LAYOUT = ('timestamp', 'type', 'amount', 'to', 'from')
DEFAULT_TIMESTAMP_FORMAT = '%b %d %Y'

INPUT_FILES_PATH = 'input/data/'
