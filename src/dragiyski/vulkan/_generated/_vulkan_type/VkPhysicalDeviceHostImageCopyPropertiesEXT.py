import ctypes, sys

class VkPhysicalDeviceHostImageCopyPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('copySrcLayoutCount', ctypes.c_uint32),
        ('pCopySrcLayouts', ctypes.POINTER(ctypes.c_int)),
        ('copyDstLayoutCount', ctypes.c_uint32),
        ('pCopyDstLayouts', ctypes.POINTER(ctypes.c_int)),
        ('optimalTilingLayoutUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('identicalMemoryTypeRequirements', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceHostImageCopyPropertiesEXT
