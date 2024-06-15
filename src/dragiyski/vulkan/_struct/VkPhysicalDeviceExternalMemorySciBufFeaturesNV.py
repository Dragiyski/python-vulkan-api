import ctypes, sys

class VkPhysicalDeviceExternalMemorySciBufFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciBufImport', ctypes.c_uint32),
        ('sciBufExport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalMemorySciBufFeaturesNV