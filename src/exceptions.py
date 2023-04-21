import sys #importing sys allows access to some variables and functions used or maintained by the interpreter
from src.logger import logging 

def error_message_details(error, error_detail: sys):
    """Generate a detailed error message with file name, line number, and error message.
    Args:
        error (Exception): The error that occurred.
        error_detail (module): A reference to the sys module.
    Returns:
        str: The formatted error message.
    """
    # Extract the traceback information using the `exc_info` method of the `error_detail` module and unpack it to three variables.
    _, _, exc_tb = error_detail.exc_info()
    # Extract the filename of the code that raised the error.
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format the error message with the extracted information.
    error_message = 'Error in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message  # Return the formatted error message.
    

class CustomException(Exception):
    """Will return a detailed error message including: file name, line number and error message    
    """
    
    def __init__(self, error_message, error_detail, sys): 
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        """returns the error message as a string"""
        return self.error_message    
    
    
    