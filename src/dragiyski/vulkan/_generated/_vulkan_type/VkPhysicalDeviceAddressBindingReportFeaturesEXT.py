import ctypes

class VkPhysicalDeviceAddressBindingReportFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('reportAddressBinding', ctypes.c_uint32),
    ]

VkPhysicalDeviceAddressBindingReportFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'reportAddressBinding': ctypes.c_uint32,
}
