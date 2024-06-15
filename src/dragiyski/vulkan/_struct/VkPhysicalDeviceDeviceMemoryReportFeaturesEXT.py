import ctypes, sys

class VkPhysicalDeviceDeviceMemoryReportFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceMemoryReport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDeviceMemoryReportFeaturesEXT
