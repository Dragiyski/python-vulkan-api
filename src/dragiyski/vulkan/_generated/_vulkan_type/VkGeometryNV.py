import ctypes

class VkGeometryNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'geometryType': ctypes.c_int,
            'geometry': VkGeometryDataNV,
            'flags': ctypes.c_uint32,
        }


from .VkGeometryDataNV import VkGeometryDataNV

VkGeometryNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]
