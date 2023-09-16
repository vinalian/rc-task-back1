import datetime

__all__ = [
    'Script_error'
]


class Script_error(Exception):
    def __init__(self, function_name: str, message: str or None = None):
        self.message = message
        self.function_name = function_name

    def __create_error_string(self):
        base_error_string = f'[Error] at {datetime.datetime.now()} | Function: {self.function_name}'
        if self.message:
            base_error_string += f' |  Message: {self.message}'

        return base_error_string

    def __str__(self):
        base_error_string = self.__create_error_string()
        return base_error_string
