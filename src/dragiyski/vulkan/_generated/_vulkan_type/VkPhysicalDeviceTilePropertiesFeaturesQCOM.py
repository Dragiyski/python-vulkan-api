import ctypes

class VkPhysicalDeviceTilePropertiesFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('tileProperties', ctypes.c_uint32),
    ]

VkPhysicalDeviceTilePropertiesFeaturesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'tileProperties': ctypes.c_uint32,
}
