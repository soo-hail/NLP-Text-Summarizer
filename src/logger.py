# Custom-Logging. Build on top of inbuilt 'logging-module'.
import os
import sys
import logging
from datetime import datetime

log_dir = os.path.join(os.getcwd(), 'logs') 
os.makedirs(log_dir, exist_ok=True)

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(log_dir, log_file)

# CUSTOMIZE LOGGING-MODULE.
# Basic Configuration for logging(recording) information during execution. 
logging.basicConfig(
    # Parameters.
    filename = logs_path, # Where the logs should be saved(messages are written in this file).
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s", # Fomrate fot the log-message.
    level = logging.INFO # SET LOGGING LEVEL TO "INFO".
)



