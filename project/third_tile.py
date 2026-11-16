import lvgl as lv
from tile_colors import apply_tile_colors

class PageThree:

    def __init__(self, tile):
        #Titel
        self.tile3_label = lv.label(tile)
        self.tile3_label.set_text("Settings")
        self.tile3_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile3_label.align(lv.ALIGN_TOP_LEFT, 50, 20)
        apply_tile_colors(tile)

        # Transport Typ
        self.transport_type = lv.dropdown(tile)
        self.transport_type.set_options("All\nBus\nTrain\nFerry")
        self.transport_type.set_style_text_font(lv.font_montserrat_14, 0)
        self.transport_type.align(lv.ALIGN.TOP_LEFT, 30, 50)