import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# MQTT Broker
TOPIC = os.getenv("TOPIC")
BROKER_PORT = os.getenv("BROKER_PORT")
BROKER_USER = os.getenv("BROKER_USER")
BROKER_PASSWORD = os.getenv("BROKER_PASSWORD")
BROKER_ADDRESS = os.getenv("BROKER_ADDRESS")

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Cameras
RTSP_URL = os.getenv("RTSP_URL")
CHANNELS = os.getenv("CHANNELS").split(",")

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent