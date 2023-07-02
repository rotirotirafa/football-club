class BaseExceptionWithCode(Exception):
    """
    Name: Nome da exception
    Ex: Exception propriamente dita
    Code: Código da exception, catalogada na documentação do software.
    """
    def __init__(self, name: str, ex: str, code: int = None):
        self.name = name
        self.code = code
        self.ex = ex
