class ConsoleFormatter:
    @staticmethod
    def print_section_header(message: str) -> None:
        # Using asterisks for a clean look
        border = "*" * (len(message) + 4)
        print(border)
        print(f"* {message} *")
        print(border)

    @staticmethod
    def print_subheader(message: str) -> None:
        # Using dashes for subheader
        border = "-" * (len(message) + 4)
        print(border)
        print(f"| {message} |")
        print(border)
