import sys
import time

import lvgl as lv
import network

import wifi

from board_lvgl import start_board
from debug_log import log
from tile_colors import apply_tile_colors

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

        """ Tile 1 """
        
        # Titel
        self.tile1_label = lv.label(self.tile1)
        self.tile1_label.set_text("Public Transport:")
        self.tile1_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile1_label.center()
        with open ("settings.txt","r") as s:
            s.readline()
            dark = True
            if (s.readline() == "Light"):
                dark = False
            apply_tile_colors(self.tile1, dark)

        
        #Grupp Nummer
        self.group_number = lv.label(self.tile1)
        self.group_number.set_text("Group 20")
        self.group_number.set_style_text_font(lv.font_montserrat_14, 0)
        self.group_number.align(lv.ALIGN.TOP_LEFT, 10, 10)
        # self.group_number.set_style_text_color(lv.color_hex(0x000000), 0)
            
        #Version
        self.version_label = lv.label(self.tile1)
        self.version_label.set_text("Version: 1.0")
        self.version_label.set_style_text_font(lv.font_montserrat_14, 0)
        self.version_label.align(lv.ALIGN.BOTTOM_LEFT, 10, -10)
        # self.version_label.set_style_text_color(lv.color_hex(0x000000), 0)
        
        #Gruppmedlemmar
        self.members_label = lv.label(self.tile1)
        self.members_label.set_text("Lucas, Matheo, William, Alex, Sam")
        self.members_label.set_style_text_font(lv.font_montserrat_14, 0)
        self.members_label.align(lv.ALIGN.TOP_RIGHT, -10, 10)
        # self.members_label.set_style_text_color(lv.color_hex(0x000000), 0)
        
        """ Tile 2 """
        
        self.tile2_label = lv.label(self.tile2)
        self.tile2_label.set_text("Welcome to the workshop")
        self.tile2_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile2_label.center()
        with open ("settings.txt","r") as s:
            s.readline()
            dark = True
            if (s.readline() == "Light"):
                dark = False
            apply_tile_colors(self.tile2, dark)

        """ Tile 3 """

        #Titel
        self.tile3_label = lv.label(self.tile3)
        self.tile3_label.set_text("Settings:")
        self.tile3_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile3_label.align(lv.ALIGN.TOP_LEFT, 235, 30)
        with open ("settings.txt","r") as s:
            s.readline()
            dark = True
            if (s.readline() == "Light"):
                dark = False
            apply_tile_colors(self.tile3, dark)
        
        # Transport Typ: Label
        self.transport_type_l = lv.label(self.tile3)
        self.transport_type_l.set_text("Transport Type:")
        self.transport_type_l.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type_l.align(lv.ALIGN.TOP_LEFT, 60, 120)
        
        # Transport Typ: Dropdown
        self.transport_type = lv.dropdown(self.tile3)
        self.transport_type.set_options("All\nBus\nTrain\nFerry")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_LEFT, 55, 140)

        # Activates whenever the selected option changes
        self.transport_type.add_event_cb(self.on_change_transport_type, lv.EVENT.VALUE_CHANGED, None)

        # Makes sure the dropdown starts with the default setting as its "selected" option
        with open("settings.txt", "r") as s:
            self.transport_type.set_selected(self.transport_type.get_option_index(s.readline().strip()))
        
        # Color Scheme: Label
        self.color_scheme_l = lv.label(self.tile3)
        self.color_scheme_l.set_text("Color Scheme:")
        self.color_scheme_l.set_style_text_font(lv.font_montserrat_14, 0)
        self.color_scheme_l.align(lv.ALIGN.TOP_RIGHT, -60, 120)
                
        # Color Scheme: Dropdown
        self.color_scheme = lv.dropdown(self.tile3)
        self.color_scheme.set_options("Light\nDark")
        self.color_scheme.set_style_text_font(lv.font_montserrat_14, 0)
        self.color_scheme.align(lv.ALIGN.TOP_RIGHT, -55, 140)

        # Makes sure the dropdown starts with the default setting as its "selected" option
        with open("settings.txt", "r") as s:
            s.readline() # Color scheme setting is on the second like, so we burn a "readline" to get there
            self.color_scheme.set_selected(self.color_scheme.get_option_index(s.readline().strip()))

        # Activates/deactivates dark mode
        self.color_scheme.add_event_cb(self.on_change_color_scheme, lv.EVENT.VALUE_CHANGED, None)

    def on_change_color_scheme(self, _event):
        dark = True
        if (self.color_scheme.get_selected() == 0):
            dark = False

        apply_tile_colors(self.tile1, dark)
        apply_tile_colors(self.tile2, dark)
        apply_tile_colors(self.tile3, dark)
        self.save_default_settings()

    def on_change_transport_type(self, _event):
        self.save_default_settings()

    def save_default_settings(self):
        with open("settings.txt", "w") as s:
            log("fixar snart")
            #s.write(f"{self.transport_type.get_selected_str(None,64)}\n{self.color_scheme.get_selected_str(None,64)}")


try:
    app = Application()
except Exception as error:
    log("FATAL: %r" % (error,))
    sys.print_exception(error)
    raise
