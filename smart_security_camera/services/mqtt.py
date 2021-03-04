import cv2
import paho.mqtt.client as mqtt
from config import settings

from .detection import YoloDetection
from .video import VideoStream


class MQTTClient:
    def __init__(self) -> None:
        self.__client = mqtt.Client()
        self.__client.username_pw_set(settings.BROKER_USER, settings.BROKER_PASSWORD)
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.connect(settings.BROKER_ADDRESS, settings.BROKER_PORT)

        self.__yolo_cnn = YoloDetection()
        self.__video_stream = VideoStream()

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
        if msg.payload.decode() != "on":
            return

        for channel in settings.CHANNELS:
            rtsp = settings.RTSP_URL.replace("channel=1", f"channel={channel}")
            self.__video_stream.set_rtsp_url(rtsp)
            frame = self.__video_stream.get_frame()
            self.__yolo_cnn.detect(frame, channel)

    def start(self):
        self.__client.loop_forever()
