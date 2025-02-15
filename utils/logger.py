# utils/logger.py

import logging
import os
from datetime import datetime

# Define the logs directory
LOGS_DIR = "logs"

def setup_logger():
    """
    Set up a logger to log agent interactions.
    Logs are saved in the 'logs' directory.
    """
    # Create the logs directory if it doesn't exist
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    # Generate a log filename with a timestamp
    log_filename = f"agent_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_filepath = os.path.join(LOGS_DIR, log_filename)

    # Configure the logger
    logging.basicConfig(
        filename=log_filepath,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()

def clear_logs():
    """
    Clear all log files in the 'logs' directory.
    """
    # Check if the logs directory exists
    if not os.path.exists(LOGS_DIR):
        print(f"No logs directory found: {LOGS_DIR}")
        return

    # Find all log files in the logs directory
    log_files = [f for f in os.listdir(LOGS_DIR) if f.startswith("agent_logs_") and f.endswith(".log")]
    for log_file in log_files:
        try:
            os.remove(os.path.join(LOGS_DIR, log_file))
            print(f"Deleted log file: {log_file}")
        except Exception as e:
            print(f"Failed to delete log file {log_file}: {e}")

# Initialize the logger
logger = setup_logger()