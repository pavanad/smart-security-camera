import paho.mqtt.client as mqtt

from config import settings


class MQTTClient:
    def __init__(self) -> None:
        self.__client = mqtt.Client()
        self.__client.username_pw_set(settings.BROKER_USER, settings.BROKER_PASSWORD)
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.connect(settings.BROKER_ADDRESS, settings.BROKER_PORT)

    def __on_connect(self, client, userdata, flags, rc):
        """
        The callback for when the client receives a CONNACK response from the server.
        """
        print("Connected with result code " + str(rc))

        # subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.__client.subscribe(settings.TOPIC)

    def __on_message(self, client, userdata, msg):
        """
        The callback for when a PUBLISH message is received from the server.
        """
        print(msg.topic + " " + str(msg.payload))

    def start(self):
        self.__client.loop_forever()
