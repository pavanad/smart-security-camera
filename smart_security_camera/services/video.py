import logging
import os

import cv2
from numpy.core.numeric import ndarray

from .bot import BotTelegram
from .messages import Messages


class VideoStream:
    def __init__(self) -> None:
        self.__rtsp_url = ""
        self.__capture = None
        self.__logger = logging.getLogger(__name__)
        self.__logger.info("Creating video stream object")

        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

    def __open(self):
        self.__capture = cv2.VideoCapture(self.__rtsp_url, cv2.CAP_FFMPEG)
        if not self.__capture.isOpened():            
            BotTelegram().send_message(Messages.ERROR_CONNECTION)
            raise Exception("Error trying to open the camera")

    def __release(self):
        if self.__capture is not None:
            self.__capture.release()

    def set_rtsp_url(self, rtsp_url: str):
        self.__rtsp_url = rtsp_url

    def get_frame(self) -> ndarray:
        self.__open()
        ret, frame = self.__capture.read()
        self.__release()
        return frame
