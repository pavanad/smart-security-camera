import os

import cv2
from numpy.core.numeric import ndarray


class VideoStream:
    def __init__(self) -> None:
        self.__rtsp_url = ""
        self.__capture = None
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

    def __open(self):
        self.__capture = cv2.VideoCapture(self.__rtsp_url, cv2.CAP_FFMPEG)
        if not self.__capture.isOpened():
            # logger.error("Error trying to open the camera")
            # BotTelegram().send_message(Messages.ERROR_CONNECTION)
            return

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
