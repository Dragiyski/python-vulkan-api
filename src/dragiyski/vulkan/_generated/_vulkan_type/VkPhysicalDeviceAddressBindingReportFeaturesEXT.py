import ctypes, sys

class VkPhysicalDeviceAddressBindingReportFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('reportAddressBinding', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceAddressBindingReportFeaturesEXT
