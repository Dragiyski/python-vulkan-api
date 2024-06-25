import ctypes

class VkConformanceVersion(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint8),
        ('minor', ctypes.c_uint8),
        ('subminor', ctypes.c_uint8),
        ('patch', ctypes.c_uint8),
    ]

VkConformanceVersion._type_ = {
    'major': ctypes.c_uint8,
    'minor': ctypes.c_uint8,
    'subminor': ctypes.c_uint8,
    'patch': ctypes.c_uint8,
}
