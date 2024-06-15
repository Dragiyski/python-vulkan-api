import ctypes, sys

class VkExportMetalDeviceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mtlDevice', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkExportMetalDeviceInfoEXT
