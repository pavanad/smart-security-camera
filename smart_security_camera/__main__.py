from services.mqtt import MQTTClient


def main():
    mqtt_client = MQTTClient()
    mqtt_client.start()


if __name__ == "__main__":
    main()
