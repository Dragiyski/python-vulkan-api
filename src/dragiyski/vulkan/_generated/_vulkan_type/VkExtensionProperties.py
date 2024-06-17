import ctypes, sys

class VkExtensionProperties(ctypes.Structure):
    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExtensionProperties
