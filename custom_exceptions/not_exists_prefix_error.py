class NotExistsPrefixError(Exception):
    def __init__(self, text: str) -> None:
        self.txt: str = text
