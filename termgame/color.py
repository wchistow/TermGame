def from_rgb_to_string(r: int, g: int, b: int) -> str:
    for c in r, g, b:
        assert c in range(0, 256)
        assert type(c) == int

    if 0 <= r < 21 and 0 <= g < 21 and 0 <= b < 21:
        return '\033[0;30m'  # black
    elif 229 < r < 256 and 229 < g < 256 and 229 < b < 256:
        return '\033[1;37m'  # white
