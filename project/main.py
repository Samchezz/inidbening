import sys
import time

import lvgl as lv
import network

import wifi

from board_lvgl import start_board
from debug_log import log

from first_tile import PageOne
from second_tile import PageTwo
from third_tile import PageThree

from secrets import WIFI_SSID, WIFI_PASSWORD


class Application:
    def __init__(self):
        self.display, self.touch, self.handler = start_board()
        self.create_ui()
        self.wifi = wifi.Wifi()
        log("student application ready")

    def create_ui(self):
        'Function: Creates UI'
        self.tileview = lv.tileview(lv.screen_active())
        self.tileview.set_size(600, 450)
        self.tileview.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

        self.tile1 = self.tileview.add_tile(0, 0, lv.DIR.RIGHT)
        self.tile2 = self.tileview.add_tile(1, 0, lv.DIR.LEFT | lv.DIR.RIGHT)
        self.tile3 = self.tileview.add_tile(2, 0, lv.DIR.LEFT)

        # Each tiles' UI is created in a separate class in a separate file. This is to try and avoid merge conflicts in GitHub
        self.page_one = PageOne(self.tile1)
        self.page_two = PageTwo(self.tile2)
        self.page_three = PageThree(self.tile3)


try:
    app = Application()
except Exception as error:
    log("FATAL: %r" % (error,))
    sys.print_exception(error)
    raise
