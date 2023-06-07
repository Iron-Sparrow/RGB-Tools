class rgb:
    def __init__(self, r:int, g:int, b:int):
        if r not in range(0, 255):
            raise ValueError(f"r must be a value inbetween 0 and 255. Currently: {r}")
        if g not in range(0, 255):
            raise ValueError(f"r must be a value inbetween 0 and 255. Currently: {g}")
        if b not in range(0, 255):
            raise ValueError(f"r must be a value inbetween 0 and 255. Currently: {b}")
        self.r = r
        self.g = g
        self.b = b