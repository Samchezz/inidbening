import lvgl as lv
from tile_colors import apply_tile_colors

class PageTwo:

    def __init__(self, tile):
        """Andra sidan """

        self.tile2_label = lv.label(tile)
        self.tile2_label.set_text("Welcome to the workshop")
        self.tile2_label.set_style_text_font(lv.font_montserrat_28, 0)
        self.tile2_label.center()
        apply_tile_colors(tile, False)