import logging

from services.mqtt import MQTTClient


def main():

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s (%(name)s) %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="logs/smart_security.log",
        filemode="a",
    )
    logger = logging.getLogger(__name__)
    logger.info("Initializing object detection service")

    try:
        mqtt_client = MQTTClient()
        mqtt_client.start()
    except Exception as error:
        logger.error(error)


if __name__ == "__main__":
    main()
