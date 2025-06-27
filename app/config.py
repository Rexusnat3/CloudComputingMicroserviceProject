import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SMTP Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# Default sender email
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

# Validate that critical config variables are present
required_vars = {
    "SMTP_SERVER": SMTP_SERVER,
    "SMTP_USERNAME": SMTP_USERNAME,
    "SMTP_PASSWORD": SMTP_PASSWORD,
    "SENDER_EMAIL": SENDER_EMAIL,
}

missing = [key for key, value in required_vars.items() if not value]
if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
