'''These lines import the necessary modules for logging, 
operating system interaction, and working with dates and times'''

import logging
import os 
from datetime import datetime

"""This line creates a log file name based on the current date and time, 
formatted as a string with the month, day, year, hour, minute, and second."""

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

"""This line creates a logs_path variable by joining the current working directory, 
a subdirectory called "logs," and the LOG_FILE name."""
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)


"""This line creates the directory specified in logs_path if it doesn't already exist,
with the exist_ok parameter set to True to avoid raising an exception
if the directory already exists."""
os.makedirs(logs_path,exist_ok=True)

"""This line creates a full path to the log file by joining the logs_path 
and LOG_FILE variables."""
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

"""This line sets up basic configuration for logging. 
It specifies the log file path, a format string for log messages,
and the logging level to use. The format string includes the date and time,
line number, logger name, log level, and log message. The logging level is set to INFO, 
which means that messages with a severity level of
INFO or higher (such as WARNING and ERROR) will be recorded in the log file."""

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s",
    level=logging.INFO,
    
)