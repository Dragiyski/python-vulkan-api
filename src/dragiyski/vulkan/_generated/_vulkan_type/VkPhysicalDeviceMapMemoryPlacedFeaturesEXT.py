import ctypes

class VkPhysicalDeviceMapMemoryPlacedFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'memoryMapPlaced': ctypes.c_uint32,
            'memoryMapRangePlaced': ctypes.c_uint32,
            'memoryUnmapReserve': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryMapPlaced', ctypes.c_uint32),
        ('memoryMapRangePlaced', ctypes.c_uint32),
        ('memoryUnmapReserve', ctypes.c_uint32),
    ]
