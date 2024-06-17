import ctypes, sys

class VkImageCompressionPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionFlags', ctypes.c_uint32),
        ('imageCompressionFixedRateFlags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkImageCompressionPropertiesEXT
