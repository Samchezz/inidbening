import lvgl as lv
from tile_colors import apply_tile_colors

class PageThree:

    def __init__(self, tile):

        #Titel
        self.tile3_label = lv.label(tile)
        self.tile3_label.set_text("Settings:")
        self.tile3_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile3_label.align(lv.ALIGN.TOP_LEFT, 235, 30)
        apply_tile_colors(tile, False)

        # Transport Typ: Label
        self.transport_type = lv.label(tile)
        self.transport_type.set_text("Transport Type:")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_LEFT, 60, 120)

        # Transport Typ: Dropdown
        self.transport_type = lv.dropdown(tile)
        self.transport_type.set_options("All\nBus\nTrain\nFerry")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_LEFT, 55, 140)

        # Transport Typ: Label
        self.transport_type = lv.label(tile)
        self.transport_type.set_text("Color Scheme:")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_RIGHT, -60, 120)
        
        # Transport Typ: Dropdown
        self.transport_type = lv.dropdown(tile)
        self.transport_type.set_options("Light\nDark")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_RIGHT, -55, 140)