import lvgl as lv
from tile_colors import apply_tile_colors


class PageOne:

    def __init__(self, tile):
        #Titel
        self.tile1_label = lv.label(tile)
        self.tile1_label.set_text("Public Transport:")
        self.tile1_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile1_label.center()
        self.apply_tile_colors(tile, self.tile1_label, False)

        #Grupp Nummer
        self.group_number = lv.label(tile)
        self.group_number.set_text("Group 20")
        self.group_number.set_style_text_font(lv.font_montserrat_14, 0)
        self.group_number.align(lv.ALIGN.TOP_LEFT, 10, 10)
        self.group_number.set_style_text_color(lv.color_hex(0x000000), 0)
    
        #Version
        self.version_label = lv.label(tile)
        self.version_label.set_text("Version: 1.0")
        self.version_label.set_style_text_font(lv.font_montserrat_14, 0)
        self.version_label.align(lv.ALIGN.BOTTOM_LEFT, 10, -10)
        self.version_label.set_style_text_color(lv.color_hex(0x000000), 0)

        #Gruppmedlemmar
        self.members_label = lv.label(tile)
        self.members_label.set_text("Lucas, Matheo, William, Alex, Sam")
        self.members_label.set_style_text_font(lv.font_montserrat_14, 0)
        self.members_label.align(lv.ALIGN.TOP_RIGHT, -10, 10)
        self.members_label.set_style_text_color(lv.color_hex(0x000000), 0)