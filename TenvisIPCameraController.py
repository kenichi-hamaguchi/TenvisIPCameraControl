#!/usr/bin/env python

import requests
from enum import Enum


CGI_URL = 'http://192.168.3.239:8080/cgi-bin/control.cgi'


class MOTION_CODE(Enum):
    MOVE       = 2
    STOP       = 3

class DIRECTION(Enum):
    UP         = 1
    DOWN       = 2
    RIGHT      = 3
    LEFT       = 4
    UP_RIGHT   = 5
    UP_LEFT    = 6
    DOWN_RIGHT = 7
    DOWN_LEFT  = 8

class TenvisIPCameraController:
    def __init__(self):
        self._session = requests.Session()
        self._session.auth = ('admin', 'admin')
     
    def __del__(self):
        self._session.close()

    def move(self, direction):
        if isinstance(direction, DIRECTION):
            self.__sendRequest(MOTION_CODE.MOVE, direction)

    def stop(self):
        for d in DIRECTION:
            self.__sendRequest(MOTION_CODE.STOP, d)

    def __sendRequest(self, motion_code, direction, timeout_sec=1):
        payload = {'action': 'cmd', 'code': motion_code.value, 'value': direction.value}
        self._session.get(CGI_URL, params=payload, timeout=timeout_sec)

if __name__ == '__main__':
    import time
    
    print("======= TEST START =======")
    tcc = TenvisIPCameraController()
    for d in DIRECTION:
        print(d)
        tcc.move(d)
        time.sleep(1)
        tcc.stop()
        time.sleep(1)
    print("======= TEST END =======")
