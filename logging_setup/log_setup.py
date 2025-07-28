import logging
import os

def setup_logger(log_file_name: str, log_dir: str = "logs", logger_name: str = None) -> logging.Logger:
    
    os.makedirs(log_dir, exist_ok=True)
    
    if logger_name is None:
        logger_name = os.path.splitext(log_file_name)[0]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # File handler
        log_file_path = os.path.join(log_dir, log_file_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
