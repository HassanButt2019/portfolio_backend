import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logger = logging.getLogger("portfolio_logger")
logger.setLevel(logging.INFO)

# Log to a file with rotation
handler = RotatingFileHandler("portfolio.log", maxBytes=5000000, backupCount=3)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(handler)
