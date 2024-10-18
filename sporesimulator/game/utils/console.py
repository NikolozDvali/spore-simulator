import shutil


class ConsoleFormatter:
    MAX_LENGTH = shutil.get_terminal_size().columns

    @staticmethod
    def print_section_header(message: str, character: str = "=") -> None:
        formatted_message = message.center(ConsoleFormatter.MAX_LENGTH)
        line = character * ConsoleFormatter.MAX_LENGTH
        print(line)
        print(formatted_message)
        print(line)

    @staticmethod
    def print_subheader(message: str) -> None:
        formatted_message = message.center(ConsoleFormatter.MAX_LENGTH)
        line = "-" * ConsoleFormatter.MAX_LENGTH
        print(line)
        print(formatted_message)
        print(line)
