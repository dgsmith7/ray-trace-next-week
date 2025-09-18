import math

from Vec3 import Color

class Texture:
    def value(self, u, v, p):
        """
        Abstract method to get the color value at texture coordinates (u, v) and point p.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("Texture subclasses must implement the value method.")

class SolidColor(Texture):
    def __init__(self, albedo):
        if isinstance(albedo, Color):
            self.albedo = albedo
        else:
            # Accepts tuple/list or individual RGB values
            self.albedo = Color(*albedo)

    def value(self, u, v, p):
        return self.albedo

# CheckerTexture: supports both (scale, even, odd) and (scale, c1, c2) signatures
class CheckerTexture(Texture):
    def __init__(self, scale, even, odd=None):
        self.inv_scale = 1.0 / scale if scale != 0 else 1.0
        if odd is None:
            # If only two colors are given, treat as (scale, c1, c2)
            self.even = SolidColor(even)
            self.odd = SolidColor(scale)
        else:
            self.even = even if isinstance(even, Texture) else SolidColor(even)
            self.odd = odd if isinstance(odd, Texture) else SolidColor(odd)

    def value(self, u, v, p):
        x_int = int(math.floor(self.inv_scale * p.x()))
        y_int = int(math.floor(self.inv_scale * p.y()))
        z_int = int(math.floor(self.inv_scale * p.z()))
        is_even = (x_int + y_int + z_int) % 2 == 0
        return self.even.value(u, v, p) if is_even else self.odd.value(u, v, p)