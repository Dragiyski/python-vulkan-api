import ctypes

class VkSamplerCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'magFilter': ctypes.c_int,
            'minFilter': ctypes.c_int,
            'mipmapMode': ctypes.c_int,
            'addressModeU': ctypes.c_int,
            'addressModeV': ctypes.c_int,
            'addressModeW': ctypes.c_int,
            'mipLodBias': ctypes.c_float,
            'anisotropyEnable': ctypes.c_uint32,
            'maxAnisotropy': ctypes.c_float,
            'compareEnable': ctypes.c_uint32,
            'compareOp': ctypes.c_int,
            'minLod': ctypes.c_float,
            'maxLod': ctypes.c_float,
            'borderColor': ctypes.c_int,
            'unnormalizedCoordinates': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('magFilter', ctypes.c_int),
        ('minFilter', ctypes.c_int),
        ('mipmapMode', ctypes.c_int),
        ('addressModeU', ctypes.c_int),
        ('addressModeV', ctypes.c_int),
        ('addressModeW', ctypes.c_int),
        ('mipLodBias', ctypes.c_float),
        ('anisotropyEnable', ctypes.c_uint32),
        ('maxAnisotropy', ctypes.c_float),
        ('compareEnable', ctypes.c_uint32),
        ('compareOp', ctypes.c_int),
        ('minLod', ctypes.c_float),
        ('maxLod', ctypes.c_float),
        ('borderColor', ctypes.c_int),
        ('unnormalizedCoordinates', ctypes.c_uint32),
    ]
