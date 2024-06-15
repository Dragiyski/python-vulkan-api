import ctypes, sys

class VkLayerSettingEXT(ctypes.Structure):
    _fields_ = [
        ('pLayerName', ctypes.c_char_p),
        ('pSettingName', ctypes.c_char_p),
        ('type', ctypes.c_int),
        ('valueCount', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkLayerSettingEXT
