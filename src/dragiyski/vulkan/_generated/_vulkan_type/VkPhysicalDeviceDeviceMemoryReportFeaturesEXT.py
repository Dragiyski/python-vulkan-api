import ctypes

class VkPhysicalDeviceDeviceMemoryReportFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceMemoryReport', ctypes.c_uint32),
    ]

VkPhysicalDeviceDeviceMemoryReportFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceMemoryReport': ctypes.c_uint32,
}
