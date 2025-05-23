import sys
from src.logger import logging

def error_message_details(error, error_details:sys):
    _,_,ex_tb = error_details.exc_info()
    file_name = ex_tb.tb_frame.f_code.co_filename
    line_number = ex_tb.tb_lineno
    error_message = f'Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]'

    return error_message


class CustomException(Exception):
    def __init__ (self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)