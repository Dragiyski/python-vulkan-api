import ctypes, sys

class VkPhysicalDeviceFaultFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceFault', ctypes.c_uint32),
        ('deviceFaultVendorBinary', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFaultFeaturesEXT
