import logging


class Logs:

    logging.basicConfig(filename='see.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

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
        self.logger.info(self.msg_format)

    def warning(self):
        self.logger.warning(self.msg_format)

    def error(self):
        self.logger.error(self.msg_format)
