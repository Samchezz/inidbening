#Class for Wi-Fi connection and cheking it status.
#By default it trying to reconnect to WlAN. 

import network
import time


from secrets import WIFI_SSID, WIFI_PASSWORD
from debug_log import log

class Wifi:
    def __init__(self):
        'Function: Connects to WiFi'
        log("connecting to Wi-Fi SSID: " + WIFI_SSID)
        self.station = network.WLAN(network.STA_IF)
        self.station.active(True)
        self.station.connect(WIFI_SSID, WIFI_PASSWORD)
        started = time.ticks_ms()
        while (not self.station.isconnected() and
               time.ticks_diff(time.ticks_ms(), started) < 15_000):
            time.sleep_ms(250)
        log("Wi-Fi connected" if self.station.isconnected()
            else "Wi-Fi could not connect (timeout)")

    def wifi_conection(self):
        return self.station.isconnected()