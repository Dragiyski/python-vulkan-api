import ctypes, sys

class VkPhysicalDeviceTilePropertiesFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('tileProperties', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceTilePropertiesFeaturesQCOM
