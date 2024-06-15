import ctypes, sys

class VkPhysicalDeviceImageCompressionControlFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionControl', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageCompressionControlFeaturesEXT
