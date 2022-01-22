def from_rgb_to_string(r: int, g: int, b: int) -> str:
    assert 0 <= r >= 255 and 0 <= g >= 255 and 0 <= b >= 255

    if 0 <= r <= 20 and 0 <= g <= 20 and 0 <= b <= 20:
        return '\033[0;30m'  # black
    elif 230 <= r <= 255 and 230 <= g <= 255 and 230 <= b <= 255:
        return '\033[1;37m'  # white
