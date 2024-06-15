import ctypes, sys

class VkPhysicalDeviceExtendedDynamicState3PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicPrimitiveTopologyUnrestricted', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExtendedDynamicState3PropertiesEXT
