#!/usr/bin/env python

import cv2
from warnings import warn

MJPEG_URL = 'http://192.168.3.239:8080/vjpeg.v'


class TenvisIPCameraReader:
    def __init__(self):
        self.__src = cv2.VideoCapture()
        self.open(MJPEG_URL)

    def __del__(self):
        self.__src.release()

    def open(self, capture_device):
        ret = self.__src.open(capture_device)
        if ret is False:
            warn('Failed to open device: '+str(capture_device))

    def read(self):
        return self.__src.read()


if __name__ == '__main__':

    reader = TenvisIPCameraReader()
    while True:
        ret, frame = reader.read()
        cv2.imshow('TEST', frame)
        cv2.waitKey(33)
        # enter Esc to stop
