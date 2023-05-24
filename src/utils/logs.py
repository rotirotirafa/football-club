import json
import logging


class Logs:

    def __init__(self, code: int = None, message: str = None, exception: str = None):
        """
        code: int; Ex: 1001 - Catalog proposes
        message: str; Ex: "Cant Connect with Database"
        exception: str;
        """
        self.code = code
        self.message = message
        self.exception = exception
        self.msg_format = f"Code: {self.code} | " \
                          f"Message: {self.message} |" \
                          f" Exception: {self.exception}"

    def info(self):
        logging.info(self.msg_format)

    def warning(self):
        logging.warning(self.msg_format)

    def error(self):
        logging.error(self.msg_format)
