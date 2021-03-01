import os

from dotenv import load_dotenv

load_dotenv()

# MQTT Broker
TOPIC = os.getenv("TOPIC")
BROKER_PORT = int(os.getenv("BROKER_PORT"))
BROKER_USER = os.getenv("BROKER_USER")
BROKER_PASSWORD = os.getenv("BROKER_PASSWORD")
BROKER_ADDRESS = os.getenv("BROKER_ADDRESS")

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Cameras
RTSP_URL = os.getenv("RTSP_URL")