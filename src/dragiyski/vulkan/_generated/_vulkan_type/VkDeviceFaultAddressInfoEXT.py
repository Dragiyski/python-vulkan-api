import ctypes, sys

class VkDeviceFaultAddressInfoEXT(ctypes.Structure):
    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkDeviceFaultAddressInfoEXT
