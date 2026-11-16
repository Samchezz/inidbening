import lvgl as lv

def apply_tile_colors(tile):
    tile.set_style_bg_opa(lv.OPA.COVER, 0)
    tile.set_style_bg_color(
        lv.color_hex(0xFFFFFF), 0
    )
    tile.set_style_text_color(
        lv.color_hex(0x000000), 0
    )