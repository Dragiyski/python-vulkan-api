import ctypes, sys

class VkImportAndroidHardwareBufferInfoANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportAndroidHardwareBufferInfoANDROID
