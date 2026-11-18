import sys
import time

import lvgl as lv
import network

import wifi

from board_lvgl import start_board
from debug_log import log
from tile_colors import apply_tile_colors
from trafiklabb import get_filtered_departures


from secrets import WIFI_SSID, WIFI_PASSWORD

class Application:
    def __init__(self):
        self.display, self.touch, self.handler = start_board()
        self.wifi = wifi.Wifi()
        self.create_ui()
        self.update_departures()
        self.departures_updates = lv.timer_create(self.update_departures, 60000, None)
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
        self.tile2_label.set_text("Departures")
        self.tile2_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile2_label.align(lv.ALIGN.TOP_MID, 0, 10)

        self.table = lv.table(self.tile2)
        self.table.set_row_count(5)
        self.table.set_column_count(5)
        self.table.set_size(500,350)
        self.table.align(lv.ALIGN.TOP_MID, 0, 50)
        for i in range(5):
            self.table.set_column_width(i, 100)

        self.table.set_cell_value(0,0, "Time:")
        self.table.set_cell_value(0,1, "Line:")
        self.table.set_cell_value(0,2, "Dest.:")
        self.table.set_cell_value(0,3, "Status:")
        self.table.set_cell_value(0,4, "Tran.:")




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


def update_departures(self, update=None):
    if self.wifi.wifi_conection() is True:
        try:
            selected_transport = ["ALL", "BUS", "TRAIN", "FERRY"][self.transport_type.get_selected()]

            departures = get_filtered_departures("740032188", selected_transport)

            # Clear old departures
            for row in range(1, 5):
                for column in range(5):
                    self.table.set_cell_value(row, column, "")

            # Display new departures
            for row, x in enumerate(departures[:4]):
                self.table.set_cell_value(row + 1, 0, str(x["time"]))
                self.table.set_cell_value(row + 1, 1, str(x["line"]))
                self.table.set_cell_value(row + 1, 2, str(x["destination"]))
                self.table.set_cell_value(row + 1, 3, str(x["status"]))
                self.table.set_cell_value(row + 1, 4, str(x["transport_type"]))

        except Exception as error:
            log("Can not get departures: %r" % (error,))



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
